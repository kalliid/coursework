#ifndef SYSTEM_H
#define SYSTEM_H

#include <vector>
#include <random>
#include <algorithm>
#include "vec3.h"
#include "parameters.h"

using namespace std;

class Atom;
class Cell;
class System;

class Atom {
public:
    vec3 r;
    vec3 v;
    vec3 F;
    bool moving;

    Atom(double x, double y, double z);
    void reset_force();
    void add_F(vec3 F);
    void freeze();
    void unfreeze();
};

class Cell {
public:
    System* system;
    int index;
    int Nx, Ny, Nz;
    int cx, cy, cz;

    vector<Cell*> neighbors;
    vector<int> atoms;

    Cell(System* sys, int I, vec3 Ncells);
    void find_neighbors();
};

class System {
public:
    vec3 sys_size;
    vec3 Ncells;
    vec3 cell_size;
    vector<Atom> atoms;
    vector<Atom*> moving_atoms;
    vector<Cell> cells;
    int Natoms;
    double V;
    double rho;
    double total_energy;
    double kinetic_energy;
    double potential_energy;
    double Ushift;
    double pressure;
    double temperature;

    System(int Nc);
    void initialize_FCC_lattice(int Nc);
    void initialize_uniform_velocities(double T);
    void initialize_boltzmann_velocities(double T);
    void eliminate_drift();
    void enforce_periodic();
    void reset_all_forces();
    void reset_pressure();
    void update_pressure(int i);
    void update_pressure();
    void calc_forces_between_pair(int i, int j);
    void calculate_forces();
    void assign_atoms_to_cells();
    Cell* get_cell(int i, int j, int k);
    void update_energies();
    double kinetic_energy_of_atom(int i);
    double potential_energy_of_pair(int i, int j);

    void freeze_cylinder_system();

private:
    void construct_cells();
    void link_cells();
};



#endif // SYSTEM_H


