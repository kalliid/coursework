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

void find_Tfluct(const string thermostat, char* init_state, char* logfile, double Tbath, double tau, int iters) {
    System sys = Logger::resume_state(init_state);
    FILE* outfile = fopen(logfile, "w+");

    if (thermostat == "nsh") {
        cout << "Starting Tfluct simulation with Nose Hoover" << endl;
        Nose_hoover_integrator solver = Nose_hoover_integrator(&sys);
        solver.set_Tbath(Tbath);
        double Q = 3*sys.Natoms*tau*tau*Tbath;
        for (int i=0; i<iters; i++) {
            fprintf(outfile, "%f %f\n", i*dt, sys.temperature*T0);
            solver.vv_nosehoover_step(dt, Q);
        }
    } else if (thermostat == "and") {
        cout << "Starting Tfluct simulation with Anderssen" << endl;
        Verlet_integrator solver = Verlet_integrator(&sys);
        solver.set_Tbath(Tbath);
        for (int i=0; i<iters; i++) {
            fprintf(outfile, "%f %f\n", i*dt, sys.temperature*T0);
            solver.vv_andersen_step(dt, tau);
        }
    } else if (thermostat == "ber") {
        cout << "Starting Tfluct simulation with Berendsen" << endl;
        Verlet_integrator solver = Verlet_integrator(&sys);
        solver.set_Tbath(Tbath);
        for (int i=0; i<iters; i++) {
            fprintf(outfile, "%f %f\n", i*dt, sys.temperature*T0);
            solver.vv_berendsen_step(dt, tau);
        }
    } else if (thermostat == "none") {
        cout << "Starting Tfluct simulation with no thermostat"  << endl;
        Verlet_integrator solver = Verlet_integrator(&sys);
        solver.set_Tbath(Tbath);
        sys.start_measuring_displacement();

        for (int i=0; i<iters; i++) {
            fprintf(outfile, "%f %f\n", i*dt, sys.temperature*T0);
            solver.velocity_verlet_step(dt);
        }
    } else {
        cout << "Thermostat arg not recognized." << endl;
    }
    fclose(outfile);
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

//    char outfile1[] = "../../data/Tfluct_ber_Nc8_T800.dat";
//    char outfile2[] = "../../data/Tfluct_and_Nc8_T800.dat";
//    char outfile3[] = "../../data/Tfluct_coeff_nsh_Nc8_T800.dat";
//    char outfile4[] = "../../data/Tfluct_coeff_non_Nc8_T800.dat";

    char outfile1[] = "../../data/relfluct_nsh_Nc8_T800_tau15";
    char outfile2[] = "../../data/relfluct_nsh_Nc8_T800_tau50";
    char outfile3[] = "../../data/relfluct_nsh_Nc8_T800_tau150";
    char outfile4[] = "../../data/relfluct_nsh_Nc8_T800_tau300";

    char outfile5[] = "../../data/relfluct_ber_Nc8_T800_tau15";
    char outfile6[] = "../../data/relfluct_ber_Nc8_T800_tau50";
    char outfile7[] = "../../data/relfluct_ber_Nc8_T800_tau150";
    char outfile8[] = "../../data/relfluct_ber_Nc8_T800_tau300";

    char outfile9[] = "../../data/relfluct_and_Nc8_T800_tau15";
    char outfile10[] = "../../data/relfluct_and_Nc8_T800_tau50";
    char outfile11[] = "../../data/relfluct_and_Nc8_T800_tau150";
    char outfile12[] = "../../data/relfluct_and_Nc8_T800_tau300";

    double Tbath = 800/T0;
    int iters = 1000;

//    find_Tfluct("nsh",  init_state, outfile1, Tbath, 15*dt,  iters);
//    find_Tfluct("nsh",  init_state, outfile2, Tbath, 50*dt,  iters);
//    find_Tfluct("nsh",  init_state, outfile3, Tbath, 150*dt, iters);
//    find_Tfluct("nsh",  init_state, outfile4, Tbath, 300*dt, iters);

//    find_Tfluct("ber",  init_state, outfile5, Tbath, 15*dt,  iters);
//    find_Tfluct("ber",  init_state, outfile6, Tbath, 50*dt,  iters);
//    find_Tfluct("ber",  init_state, outfile7, Tbath, 150*dt, iters);
//    find_Tfluct("ber",  init_state, outfile8, Tbath, 300*dt, iters);

    find_Tfluct("and",  init_state, outfile9,  Tbath, 15*dt,  iters);
    find_Tfluct("and",  init_state, outfile10, Tbath, 50*dt,  iters);
    find_Tfluct("and",  init_state, outfile11, Tbath, 150*dt, iters);
    find_Tfluct("and",  init_state, outfile12, Tbath, 300*dt, iters);

//    find_rms_displacement("ber",  init_state, outfile1, Tbath, tau, iters);
//    find_rms_displacement("and",  init_state, outfile2, Tbath, tau, iters);
//    find_rms_displacement("nsh",  init_state, outfile3, Tbath, tau, iters);
//    find_rms_displacement("none", init_state, outfile4, Tbath, tau, iters);
}
