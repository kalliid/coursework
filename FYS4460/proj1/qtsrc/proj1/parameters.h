#ifndef PARAMETERS_H
#define PARAMETERS_H

// Atomic Units used
double const sigma = 3.405;
double const eps = 1.0318e-2;

double const k_b = 8.617332e-5;
double const b = 5.260/sigma; // Lattice constant for argon
double const m = 39.948;      // Mass of Argon atom in amu
double const dt = 1e-2;

double const rcut = 3.0;

// Conversion units
double const L0 = sigma;     // Å
double const t0 = 2.157e-12; // fs
double const T0 = eps/k_b;   // K
double const E0 = eps;       // eV
double const F0 = eps/sigma; // eV/Å
double const P0 = eps;


#endif // PARAMETERS_H
