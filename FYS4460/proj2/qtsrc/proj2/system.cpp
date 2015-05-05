#include "system.h"

Atom::Atom (double x, double y, double z) {
    r = vec3(x, y, z);
    v = vec3();
    F = vec3();
    moving = true;
}

void Atom::reset_force() {
    F.set(0,0,0);
}

void Atom::add_F(vec3 Finc) {
    F += Finc;
}

void Atom::freeze() {
    moving = false;
}

void Atom::unfreeze() {
    moving = true;
}

Cell::Cell(System* sys, int I, vec3 Ncells) {
    system = sys;
    index = I;
    Nx = (int) Ncells.x();
    Ny = (int) Ncells.y();
    Nz = (int) Ncells.z();

    cx = index % Nx;
    cy = index % (Nx*Ny)/Nx;
    cz = index / (Nx*Ny);
}

void Cell::find_neighbors() {
    int px = (cx + 1 + Nx) % Nx;
    int py = (cy + 1 + Ny) % Ny;
    int pz = (cz + 1 + Nz) % Nz;
    int mx = (cx - 1 + Nx) % Nx;
    int my = (cy - 1 + Ny) % Ny;
    int mz = (cz - 1 + Nz) % Nz;

    neighbors.push_back(system->get_cell(px, cy, cz));
    neighbors.push_back(system->get_cell(cx, py, cz));
    neighbors.push_back(system->get_cell(cx, cy, pz));

    neighbors.push_back(system->get_cell(px, py, cz));
    neighbors.push_back(system->get_cell(px, cy, pz));
    neighbors.push_back(system->get_cell(cx, py, pz));

    neighbors.push_back(system->get_cell(px, py, pz));

    neighbors.push_back(system->get_cell(px, py, mz));
    neighbors.push_back(system->get_cell(px, my, pz));
    neighbors.push_back(system->get_cell(mx, py, pz));

    neighbors.push_back(system->get_cell(px, my, cz));
    neighbors.push_back(system->get_cell(px, cy, mz));
    neighbors.push_back(system->get_cell(cx, py, mz));
}

System::System(int Nc) {
    sys_size = vec3(Nc*b, Nc*b, Nc*b);
    construct_cells();
    link_cells();

    double r2 = rcut*rcut;
    double r6 = r2*r2*r2;
    double r12 = r6*r6;
    Ushift = -4*(1/r12 - 1/r6);

    Natoms = 4*Nc*Nc*Nc;
    V = sys_size.x()*sys_size.y()*sys_size.z();
    rho = Natoms/V;
}

void System::initialize_FCC_lattice(int Nc) {
   // Generates the positions of all the atoms in a
   // NcxNcxNc face-centered cubic lattic
   for (int i=0; i<Nc; i++) {
       for (int j=0; j<Nc; j++) {
           for (int k=0; k<Nc; k++) {
               atoms.push_back(Atom(b*i,     b*j,     b*k));
               atoms.push_back(Atom(b*i+b/2, b*j+b/2, b*k));
               atoms.push_back(Atom(b*i+b/2, b*j,     b*k+b/2));
               atoms.push_back(Atom(b*i,     b*j+b/2, b*k+b/2));
           }
       }
   }
   calculate_forces();
}

void System::initialize_uniform_velocities(double T) {
    // Generates the initial velocities of all atoms in the system
    // Each velocity is drawn independantly from a Boltzmann distribution

    // Set up RNG following Boltzmann distribution
    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<double> uniform_dist(-2*sqrt(2*T), 2*sqrt(2*T));

    for (Atom &atom : atoms)
        atom.v.set(uniform_dist(gen), uniform_dist(gen), uniform_dist(gen));
}

void System::initialize_boltzmann_velocities(double T) {
    // Generates the initial velocities of all atoms in the system
    // Each velocity is drawn independantly from a Boltzmann distribution

    // Set up RNG following Boltzmann distribution
    random_device rd;
    mt19937 gen(rd());
    normal_distribution<double> boltzmann_dist(0, sqrt(T));

    for (Atom &atom : atoms)
        atom.v.set(boltzmann_dist(gen), boltzmann_dist(gen), boltzmann_dist(gen));
}


void System::eliminate_drift() {
    // Removes any drift of the system by subtracting
    // the average velocity from all atoms
    vec3 avg_vel = vec3();
    for (Atom atom : atoms)
        avg_vel += atom.v;
    avg_vel /= atoms.size();
    for (Atom &atom : atoms)
        atom.v -= avg_vel;
}

void System::enforce_periodic() {
    for (Atom &atom : atoms)
        atom.r = (atom.r + sys_size) % sys_size;
}

void System::reset_all_forces() {
    for (Atom &atom : atoms)
        atom.reset_force();
}

void System::reset_pressure() {
    pressure = 0;
}

void System::calc_forces_between_pair(int i, int j) {
    // Force on atom j from atom i and vice versa
    // Uses the minimum image convention

    vec3 dr = atoms[j].r - atoms[i].r; // points from i to j
    dr = dr - (dr/sys_size).round()*sys_size; // minimum image convention

    double r = dr.length();
    double r2 = r*r;
    double r8 = r2*r2*r2*r2;
    double r14 = r8*r2*r2*r2;

    vec3 F = dr*24*(2*1/r14 - 1/r8)*(r<rcut);

    atoms[j].F += F;
    atoms[i].F -= F;
}

void System::calculate_forces() {
    reset_pressure();
    reset_all_forces();
    assign_atoms_to_cells();

    // Calculate all internal forces in system
    for (Cell cell : cells) {
        for (int i : cell.atoms) {
            // Local atoms
            for (int j : cell.atoms)
                if (i < j)
                    calc_forces_between_pair(i, j);

            // Neighbor atoms
            for (Cell* neighbor : cell.neighbors)
                for (int j : neighbor->atoms)
                    calc_forces_between_pair(i, j);

            update_pressure(i);
        }
    }
}

void System::construct_cells() {
    Ncells = (sys_size/rcut).floor();
    cell_size = sys_size/Ncells;

    for (int i=0; i<(int) Ncells.x()*Ncells.y()*Ncells.z(); i++)
        cells.push_back(Cell(this, i, Ncells));
}

void System::link_cells() {
    for (int i=0; i<(int) Ncells.x()*Ncells.y()*Ncells.z(); i++)
        cells[i].find_neighbors();
}

void System::assign_atoms_to_cells() {
    // Empty all cells
    for (Cell &cell : cells)
        cell.atoms.clear();

    // Put every atom into its appropriate cell
    int cx, cy, cz;
    for (size_t i=0; i<atoms.size(); i++) {
        cx = (int) atoms[i].r.x() / cell_size.x();
        cy = (int) atoms[i].r.y() / cell_size.y();
        cz = (int) atoms[i].r.z() / cell_size.z();

        get_cell(cx, cy, cz)->atoms.push_back(i);
    }
}

void System::update_energies() {
    // Re-calculate the energies of the system
    kinetic_energy = 0;
    potential_energy = 0;
    for (Cell cell : cells) {
        for (int i : cell.atoms) {
            kinetic_energy += kinetic_energy_of_atom(i);

            // Local atoms
            for (int j : cell.atoms)
                if (i < j)
                    potential_energy += potential_energy_of_pair(i,j);

            // Neighbor atoms
            for (Cell* neighbor : cell.neighbors)
                for (int j : neighbor->atoms)
                    potential_energy += potential_energy_of_pair(i,j);
        }
    }
    temperature = (2*kinetic_energy)/(3*Natoms);
    total_energy = kinetic_energy + potential_energy;
}

void System::update_pressure(int i) {
    pressure += atoms[i].F.dot(atoms[i].r);
}

void System::update_pressure() {
    pressure /= -3*V;
    pressure += rho*k_b*temperature;
}


double System::kinetic_energy_of_atom(int i) {
    // Return the kinetic energy of atom i
    double v = atoms[i].v.length();
    return 0.5*v*v;
}

double System::potential_energy_of_pair(int i, int j) {
    // Return the potential energy between atom i and j

    vec3 dr = atoms[j].r - atoms[i].r; // points from i to j
    dr = dr - (dr/sys_size).round()*sys_size; // minimum image convention

    double r = dr.length();
    double r2 = r*r;
    double r6 = r2*r2*r2;
    double r12 = r6*r6;
    return (4*(1/r12 - 1/r6) + Ushift)*(r<rcut);
}

Cell* System::get_cell(int i, int j, int k) {
    return &cells[i + j*Ncells.x() + k*Ncells.x()*Ncells.y()];
}

void System::freeze_cylinder_system() {
    vec3 center = sys_size/2;
    double cutoff = (20/L0)*(20/L0);

    for (Atom &atom : atoms) {
        vec3 diff = atom.r - center;
        if ((diff.x()*diff.x() + diff.y()*diff.y()) <= cutoff) {
            atom.freeze();
        } else {
            moving_atoms.push_back(&atom);
        }
    }
}


