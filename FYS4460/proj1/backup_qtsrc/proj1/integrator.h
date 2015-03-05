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

    void kick(float dt);
    void drift(float dt);
    void velocity_verlet_step(float dt);
    void position_verlet_step(float dt);
};

#endif // INTEGRATOR_H
