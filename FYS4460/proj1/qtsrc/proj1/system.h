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
    vec3 disp;

    Atom();
    Atom(double x, double y, double z);
    void reset_force();
    void add_F(vec3 F);
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

struct RNG {
    mt19937 gen {random_device{}()};

    normal_distribution<double> std_norm_dist{0.0, 1.0};
    uniform_real_distribution<> uniform_dist{0, 1};

    double boltzmann(double T) {
        return sqrt(T)*std_norm_dist(gen);
    }

    double rand() {
        return uniform_dist(gen);
    }
};


class System {
public:
    vec3 sys_size;
    vec3 Ncells;
    vec3 cell_size;
    vector<Atom> atoms;
    vector<Cell> cells;
    int Natoms;
    int Nc;

    double V;
    double rho;
    double total_energy;
    double kinetic_energy;
    double potential_energy;
    double Ushift;
    double pressure;
    double temperature;
    bool measure_disp;

    RNG rng;

    System(int Nc);
    System(const char filename[]);
    void initialize_FCC_lattice(int Nc);
    void initialize_uniform_velocities(double T);
    void initialize_boltzmann_velocities(double T);
    void eliminate_drift();
    void enforce_periodic();
    void reset_all_forces();
    void reset_pressure();
    void calc_forces_between_pair(int i, int j);
    void calculate_forces();
    void assign_atoms_to_cells();
    Cell* get_cell(int i, int j, int k);
    void update_energies();
    double kinetic_energy_of_atom(int i);
    double potential_energy_of_pair(int i, int j);
    void collision(int i, double Tbath);


    void start_measuring_displacement();
    void reset_displacement();
    double find_mean_displacement();

    void save_state(const char filename[]);
    void resume_state(const char filename[]);


private:
    void construct_cells();
    void link_cells();
};



//struct Foo {



////    Foo() = default;
////    Foo(mt19937::result_type seed) : eng{seed} {}

//    double bar() {
//        return std_norm_dist(gen);
//    }

//    double baz() {
//        return std_norm_dist(gen);
//    }
//};



#endif // SYSTEM_H


