#include "integrator.h"

Integrator::Integrator(System* system) {
    this->system = system;
}

void Integrator::berendsen_thermostat(double Tbath) {
    berendsen_thermostat(Tbath, 15.0);
}

void Integrator::berendsen_thermostat(double Tbath, double tau) {
    double gamma = sqrt(1 + 1/tau*(Tbath/system->temperature - 1));
    for (Atom &a : system->atoms)
        a.v *= gamma;
    system->update_energies();
    system->update_pressure();
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

void Verlet_integrator::frozen_kick(double dt) {
    for (Atom* atom : system->moving_atoms)
        atom->v += atom->F*dt;
    system->enforce_periodic();
    system->calculate_forces();
}

void Verlet_integrator::frozen_drift(double dt) {
    for (Atom* atom : system->moving_atoms)
        atom->r += atom->v*dt;
    system->enforce_periodic();
    system->calculate_forces();
}

void Verlet_integrator::frozen_velocity_verlet_step(double dt) {
    frozen_kick(dt/2);
    frozen_drift(dt);
    frozen_kick(dt/2);
    system->update_energies();
    system->update_pressure();
}

void Verlet_integrator::frozen_position_verlet_step(double dt) {
    frozen_drift(dt/2);
    frozen_kick(dt);
    frozen_drift(dt/2);
    system->update_energies();
    system->update_pressure();
}

void Verlet_integrator::velocity_verlet_step(double dt) {
    kick(dt/2);
    drift(dt);
    kick(dt/2);
    system->update_energies();
    system->update_pressure();
}

void Verlet_integrator::position_verlet_step(double dt) {
    drift(dt/2);
    kick(dt);
    drift(dt/2);
    system->update_energies();
    system->update_pressure();
}


