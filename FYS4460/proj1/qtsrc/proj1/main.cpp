#include <iostream>
#include "system.h"
#include "io.h"
#include "integrator.h"
#include "parameters.h"

using namespace std;

void equilibriate(int Nc, double Tstart, double Tend, char* statefile, int iters) {
    // Generate and initialize lattice
    System sys = System(Nc);
    sys.initialize_FCC_lattice(Nc);
    sys.initialize_boltzmann_velocities(Tstart);
    sys.eliminate_drift();

    Verlet_integrator solver = Verlet_integrator(&sys);

    // Equilibriate
    for (int i=0; i<100; i++) {
        solver.velocity_verlet_step(dt);
        cout << sys.temperature*T0 << endl;
    }

    solver.set_Tbath(Tend);

    // Thermalize
    for (int i=0; i<iters; i++) {
        solver.velocity_verlet_step(dt);
        solver.berendsen_thermostat();
        cout << sys.temperature*T0 << endl;
    }

    sys.save_state(statefile);
}

void find_T_variance(double* results, char* init_state, double Tbath, int iters) {
    System sys = Logger::resume_state(init_state);
    Verlet_integrator solver = Verlet_integrator(&sys);

    solver.set_Tbath(Tbath);

    double runningT[iters];
    double avgT;

    for (int i=0; i<iters; i++) {
        solver.velocity_verlet_step(dt);
        solver.berendsen_thermostat();

        runningT[i] = sys.temperature;
        avgT += sys.temperature;
    }

    avgT /= iters;

    double var = 0;
    for (int i=0; i<iters; i++)
           var += (runningT[i] - avgT)*(runningT[i] - avgT);
    var /= iters;

    results[0] = avgT;
    results[1] = var;
    results[2] = sqrt(var)/avgT;
}

void find_beren_rms_displacement(char* init_state, char* logfile, double Tbath, int iters) {
    System sys = Logger::resume_state(init_state);
    Verlet_integrator solver = Verlet_integrator(&sys);

    solver.set_Tbath(Tbath);

    sys.start_measuring_displacement();

    FILE* outfile = fopen(logfile, "w+");
    fprintf(outfile, "%d\n", sys.Natoms);
    fprintf(outfile, "%f\n", Tbath*T0);

    for (int i=0; i<iters; i++) {
        fprintf(outfile, "%f %f\n", i*dt, sys.find_mean_displacement());
        solver.vv_berendsen_step(dt, 15*dt);
    }

    fclose(outfile);
}

void find_and_rms_displacement(char* init_state, char* logfile, double Tbath, int iters) {
    System sys = Logger::resume_state(init_state);
    Verlet_integrator solver = Verlet_integrator(&sys);

    solver.set_Tbath(Tbath);

    sys.start_measuring_displacement();

    FILE* outfile = fopen(logfile, "w+");
    fprintf(outfile, "%d\n", sys.Natoms);
    fprintf(outfile, "%f\n", Tbath*T0);

    for (int i=0; i<iters; i++) {
        fprintf(outfile, "%f %f\n", i*dt, sys.find_mean_displacement());
        solver.vv_andersen_step(dt, 15*dt);
    }

    fclose(outfile);
}



void compare_T_to_Tbath() {
    char init_state[] = "../../data/fluctstudies_Nc4_T800";
    double Tbath = 800/T0;
    int iters = 100;

    System sys1 = Logger::resume_state(init_state);
    System sys2 = Logger::resume_state(init_state);

    Verlet_integrator solver1 = Verlet_integrator(&sys1);
    Verlet_integrator solver2 = Verlet_integrator(&sys2);

    solver1.set_Tbath(Tbath);
    solver2.set_Tbath(Tbath);

    double avgdiff = 0;

    for (int i=0; i<iters; i++) {
        printf("Berendsen: %f \t Andersen: %f \t Diff: %f \n", sys1.temperature*T0, sys2.temperature*T0, (sys1.temperature-sys2.temperature)*T0);
        avgdiff += (sys1.temperature - sys2.temperature)*T0;

        solver1.vv_berendsen_step(dt, 15*dt);
        solver2.vv_andersen_step(dt, 15*dt);
    }

    cout << avgdiff/iters << endl;
}


int main() {
    char init_state[] = "../../data/fluctstudies_Nc8_T800";
    char datafile1[] = "../../data/beren_r2_Nc8_T800";
    char datafile2[] = "../../data/anders_r2_Nc8_T800";
    double Tbath = 800/T0;
    int iters = 2000;

//    equilibriate(8, 1200/T0, Tbath, init_state, 300);

    //find_beren_rms_displacement(init_state, datafile1, Tbath, iters);
    find_and_rms_displacement(init_state, datafile2, Tbath, iters);
}




