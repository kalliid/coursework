#ifndef INTEGRATOR_H
#define INTEGRATOR_H

#include "system.h"

class Verlet_integrator {
public:
    System* system;
    double Tbath;

    Verlet_integrator(System* system);
    void set_Tbath(double T);
    void kick(double dt);
    void drift(double dt);
    void velocity_verlet_step(double dt);
    void position_verlet_step(double dt);
    void berendsen_thermostat(double tau);
    void andersen_thermostat(double tau);
    void vv_berendsen_step(double dt, double tau);
    void vv_andersen_step(double dt, double coll_freq);
};

class Nose_hoover_integrator {
public:
    System* system;
    double Tbath;
    double gamma;

    Nose_hoover_integrator(System *system);
    void set_Tbath(double T);
    void kick(double dt, double Q);
    void drift(double dt);
    void vv_nosehoover_step(double dt, double Q);
};



#endif // INTEGRATOR_H
