#ifndef SYSTEM_H
#define SYSTEM_H

#include "argon_lattice.h"
#include "vec3.h"

class Atom {
public:
    vec3 r;
    vec3 v;
    vec3 F;

    Atom(float x, float y, float z);
};

class System {
public:
    vector<Atom> atoms;

    void initialize_FCC_lattice(int Nc);
    void initialize_velocities(float T);
    void eliminate_drift();
};

#endif // SYSTEM_H


