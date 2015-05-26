#ifndef INTEGRATOR_H
#define INTEGRATOR_H

#include "system.h"

class Integrator{
public:
    System* system;
    double Tbath;

    Integrator(System* system);
    void Step();

    void set_Tbath(double T);
    void berendsen_thermostat();
    void berendsen_thermostat(double tau);
    void andersen_thermostat(double coll_freq);
};

class Verlet_integrator : public Integrator {
    using Integrator :: Integrator;

private:
    void kick(double dt);
    void drift(double dt);
public:
    void velocity_verlet_step(double dt);
    void position_verlet_step(double dt);
    void vv_berendsen_step(double dt, double tau);
    void vv_andersen_step(double dt, double coll_freq);

};



#endif // INTEGRATOR_H
