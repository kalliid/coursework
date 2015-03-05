#ifndef SYSTEM_H
#define SYSTEM_H

#include <vector>
#include <random>
#include "vec3.h"
#include "parameters.h"

using namespace std;

class Atom {
public:
    vec3 r;
    vec3 v;
    vec3 F;

    Atom(float x, float y, float z);
    void reset_force();
};

class System {
public:
    vec3 sys_size;
    vector<Atom> atoms;

    System(int Nc);
    void initialize_FCC_lattice(int Nc);
    void initialize_velocities(float T);
    void eliminate_drift();
    void enforce_periodic();
    void reset_all_forces();
    void calc_forces_between_pair(int i, int j);
    void calculate_forces();
};

#endif // SYSTEM_H


