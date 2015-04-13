#ifndef INTEGRATOR_H
#define INTEGRATOR_H

#include "system.h"

class Integrator{
public:
    System* system;

    Integrator(System* system);
    void Step();
};

class Verlet_integrator : public Integrator {
    using Integrator :: Integrator;

private:
    void kick(double dt);
    void drift(double dt);
public:
    void velocity_verlet_step(double dt);
    void position_verlet_step(double dt);
};

#endif // INTEGRATOR_H
