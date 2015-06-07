#include <iostream>
#include "system.h"
#include "io.h"
#include "integrator.h"
#include "parameters.h"

using namespace std;

void equilibriate(int Nc, double Tstart, double Tend, char* statefile, double tau, int iters) {
    // Generate and initialize lattice
    System sys = System(Nc);
    sys.initialize_FCC_lattice(Nc);
    sys.initialize_boltzmann_velocities(Tstart);
    sys.eliminate_drift();

    Verlet_integrator solver = Verlet_integrator(&sys);

    solver.set_Tbath(Tend);

    // Equilibriate
    for (int i=0; i<100; i++) {
        solver.velocity_verlet_step(dt);
        cout << sys.temperature*T0 << endl;
    }

    // Thermalize
    for (int i=0; i<iters; i++) {
        solver.vv_berendsen_step(dt, tau);
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
        solver.vv_berendsen_step(dt, 15.0);
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

void find_nsh_rms_displacement(char* init_state, char* logfile, double Tbath, int iters) {
    System sys = Logger::resume_state(init_state);
    Nose_hoover_integrator solver = Nose_hoover_integrator(&sys);

    solver.set_Tbath(Tbath);

    sys.start_measuring_displacement();

    FILE* outfile = fopen(logfile, "w+");
    fprintf(outfile, "%d\n", sys.Natoms);
    fprintf(outfile, "%f\n", Tbath*T0);

    for (int i=0; i<iters; i++) {
        fprintf(outfile, "%f %f\n", i*dt, sys.find_mean_displacement());
        solver.vv_nosehoover_step(dt, 15*dt);
    }
    fclose(outfile);
}

void ber_Tfluct(char* init_state, double Tbath, double tau, int iters) {
    System sys = Logger::resume_state(init_state);
    Verlet_integrator solver = Verlet_integrator(&sys);
    solver.set_Tbath(Tbath);
    for (int i=0; i<iters; i++) {
        solver.vv_berendsen_step(dt, tau);
        printf("%f\n", sys.temperature*T0);
    }
}

void and_Tfluct(char* init_state, double Tbath, double tau, int iters) {
    System sys = Logger::resume_state(init_state);
    Verlet_integrator solver = Verlet_integrator(&sys);
    solver.set_Tbath(Tbath);
    for (int i=0; i<iters; i++) {
        solver.vv_andersen_step(dt, tau);
        printf("%f\n", sys.temperature*T0);
    }
}

void nsh_Tfluct(char* init_state, double Tbath, double tau, int iters) {
    System sys = Logger::resume_state(init_state);
    Nose_hoover_integrator solver = Nose_hoover_integrator(&sys);
    solver.set_Tbath(Tbath);
    double Q = 3*sys.Natoms*tau*tau*Tbath;
    for (int i=0; i<iters; i++) {
        solver.vv_nosehoover_step(dt, Q);
        printf("%f\n", sys.temperature*T0);
    }
}

void find_rms_displacement(const string thermostat, char* init_state, char* logfile, double Tbath, double tau, int iters) {
    System sys = Logger::resume_state(init_state);
    FILE* outfile = fopen(logfile, "w+");

    if (thermostat == "nsh") {
        cout << "Starting simulation with Nose Hoover" << endl;
        Nose_hoover_integrator solver = Nose_hoover_integrator(&sys);
        solver.set_Tbath(Tbath);
        sys.start_measuring_displacement();
        double Q = 3*sys.Natoms*tau*tau*Tbath;

        for (int i=0; i<iters; i++) {
            fprintf(outfile, "%f %f\n", i*dt, sys.find_mean_displacement());
            solver.vv_nosehoover_step(dt, Q);
        }
    } else if (thermostat == "and") {
        cout << "Starting simulation with Anderssen" << endl;
        Verlet_integrator solver = Verlet_integrator(&sys);
        solver.set_Tbath(Tbath);
        sys.start_measuring_displacement();

        for (int i=0; i<iters; i++) {
            fprintf(outfile, "%f %f\n", i*dt, sys.find_mean_displacement());
            solver.vv_andersen_step(dt, tau);
        }
    } else if (thermostat == "ber") {
        cout << "Starting simulation with Berendsen" << endl;
        Verlet_integrator solver = Verlet_integrator(&sys);
        solver.set_Tbath(Tbath);
        sys.start_measuring_displacement();

        for (int i=0; i<iters; i++) {
            fprintf(outfile, "%f %f\n", i*dt, sys.find_mean_displacement());
            solver.vv_berendsen_step(dt, tau);
        }
    } else if (thermostat == "none") {
        cout << "Starting simulation with no thermostat"  << endl;
        Verlet_integrator solver = Verlet_integrator(&sys);
        solver.set_Tbath(Tbath);
        sys.start_measuring_displacement();

        for (int i=0; i<iters; i++) {
            fprintf(outfile, "%f %f\n", i*dt, sys.find_mean_displacement());
            solver.velocity_verlet_step(dt);
        }
    } else {
        cout << "Thermostat arg not recognized." << endl;//    double Q = 3*sys2.Natoms*tau*tau*Tbath;

    }
    fclose(outfile);
}


int main() {
    char init_state[] = "../../data/fluctstudies_Nc8_T800.state";

    char outfile1[] = "../../data/diffusion_coeff_ber_Nc8_T800.dat";
    char outfile2[] = "../../data/diffusion_coeff_and_Nc8_T800.dat";
    char outfile3[] = "../../data/diffusion_coeff_nsh_Nc8_T800.dat";
    char outfile4[] = "../../data/diffusion_coeff_non_Nc8_T800.dat";

    double Tbath = 800/T0;
    double tau = 100*dt;
    int iters = 1000;

    find_rms_displacement("ber",  init_state, outfile1, Tbath, tau, iters);
    find_rms_displacement("and",  init_state, outfile2, Tbath, tau, iters);
    find_rms_displacement("nsh",  init_state, outfile3, Tbath, tau, iters);
    find_rms_displacement("none", init_state, outfile4, Tbath, tau, iters);
}
