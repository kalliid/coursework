#include "integrator.h"

Integrator::Integrator(System* system) {
    this->system = system;
    Tbath = 0;
}

void Integrator::set_Tbath(double T) {
    Tbath = T;
}

void Integrator::berendsen_thermostat() {
    berendsen_thermostat(15.0*dt);
}

void Integrator::berendsen_thermostat(double tau) {
    double gamma = sqrt(1 + dt/tau*(Tbath/system->temperature - 1));
    for (Atom &a : system->atoms)
        a.v *= gamma;
    system->update_energies();
}

void Integrator::andersen_thermostat(double tau) {
    double p = dt/tau;
    for (int i=0; i<system->Natoms; i++)
        if (system->rng.rand() < p)
            system->collision(i, Tbath);
}

void Verlet_integrator::kick(double dt) {
    for (Atom &atom : system->atoms)
        atom.v += atom.F*dt;
}

void Verlet_integrator::drift(double dt) {
    if (system->measure_disp) {
        for (Atom &atom : system->atoms) {
            atom.r += atom.v*dt;
            atom.disp += atom.v*dt;
          }
    } else {
        for (Atom &atom : system->atoms) {
            atom.r += atom.v*dt;
        }
    }

    system->enforce_periodic();
    system->calculate_forces();
}

void Verlet_integrator::velocity_verlet_step(double dt) {
    kick(dt/2);
    drift(dt);
    kick(dt/2);
    system->update_energies();
}

void Verlet_integrator::position_verlet_step(double dt) {
    drift(dt/2);
    kick(dt);
    drift(dt/2);
    system->update_energies();
}

void Verlet_integrator::vv_berendsen_step(double dt, double tau) {
    kick(dt/2);
    drift(dt);
    kick(dt/2);
    system->update_energies();
    berendsen_thermostat(tau);
}

void Verlet_integrator::vv_andersen_step(double dt, double coll_freq) {
    kick(dt/2);
    drift(dt);
    kick(dt/2);
    system->update_energies();
    andersen_thermostat(coll_freq);
}



