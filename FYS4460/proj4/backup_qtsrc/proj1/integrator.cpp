#include "argon_lattice.h"
#include "integrator.h"

Integrator::Integrator(System* system) {
    this->system = system;
}

void Verlet_integrator::kick(float dt) {
    for (Atom &atom : system->atoms)
        atom.v += atom.F/m*dt;
}

void Verlet_integrator::drift(float dt) {
    for (Atom &atom : system->atoms)
        atom.r += atom.v*dt;
}

void Verlet_integrator::velocity_verlet_step(float dt) {
    kick(dt/2);
    drift(dt);
    kick(dt/2);
}

void Verlet_integrator::position_verlet_step(float dt) {
    drift(dt/2);
    kick(dt);
    drift(dt/2);
}


