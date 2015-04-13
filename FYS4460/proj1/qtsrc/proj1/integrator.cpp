#include "integrator.h"

Integrator::Integrator(System* system) {
    this->system = system;
}

void Verlet_integrator::kick(double dt) {
    for (Atom &atom : system->atoms)
        atom.v += atom.F*dt;
}

void Verlet_integrator::drift(double dt) {
    for (Atom &atom : system->atoms)
        atom.r += atom.v*dt;
    system->enforce_periodic();
    system->calculate_forces();
}

void Verlet_integrator::velocity_verlet_step(double dt) {
    kick(dt/2);
    drift(dt);
    kick(dt/2);
}

void Verlet_integrator::position_verlet_step(double dt) {
    drift(dt/2);
    kick(dt);
    drift(dt/2);
}


