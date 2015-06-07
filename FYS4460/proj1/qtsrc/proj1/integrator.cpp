#include "integrator.h"

//Integrator::Integrator(System* system, double Tbath) {
//    this->system = system;
//    this->Tbath = Tbath;
//}

//Integrator::Integrator(System* system) {
//    Integrator(system, 1.0);
//}



Verlet_integrator::Verlet_integrator(System* system) {
    this->system = system;
}

void Verlet_integrator::set_Tbath(double T) {
    Tbath = T;
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

void Verlet_integrator::berendsen_thermostat(double tau) {
    double gamma = sqrt(1 + dt/tau*(Tbath/system->temperature - 1));
    for (Atom &a : system->atoms)
        a.v *= gamma;
    system->update_energies();
}

void Verlet_integrator::andersen_thermostat(double tau) {
    double p = dt/tau;
    for (int i=0; i<system->Natoms; i++)
        if (system->rng.rand() < p)
            system->collision(i, Tbath);
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


/*
NOSE-HOOVER INTEGRATOR
*/

Nose_hoover_integrator::Nose_hoover_integrator(System* system) {
    this->system = system;
}

void Nose_hoover_integrator::set_Tbath(double T) {
    Tbath = T;
    gamma = 0;
}

void Nose_hoover_integrator::kick(double dt, double Q) {
    for (Atom &atom : system->atoms)
        atom.v += (atom.F - atom.v*gamma)*dt;
    system->update_energies();
    gamma += (dt/2)*(2*system->kinetic_energy - 3*system->Natoms*Tbath)/Q;
}

void Nose_hoover_integrator::drift(double dt) {
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

void Nose_hoover_integrator::vv_nosehoover_step(double dt, double Q) {
    int N = system->Natoms;

    kick(dt/2, Q);
    drift(dt);
    kick(dt/2, Q);
}

