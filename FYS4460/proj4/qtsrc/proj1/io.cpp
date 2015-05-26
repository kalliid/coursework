#include "system.h"
#include "io.h"

Logger::Logger(System* system, const char filename[]) {
    this->system = system;
    outfile = fopen(filename, "w+");
}

Logger::~Logger(void) {
    fclose(outfile);
}

void Logger::write_header(char header[]) {
    // Writes the header for a .xyz file
    fprintf(outfile, "%zu \n", system->atoms.size());
    fprintf(outfile, "%s \n", header);
}

void Logger::write_current_state() {
    // Writes position and velocity data for all atoms
    for (Atom atom : system->atoms) {
        fprintf(outfile, "Ar ");
        fprintf(outfile, "%f %f %f ", atom.r.x(), atom.r.y(), atom.r.z());
        fprintf(outfile, "%f %f %f ", atom.v.x(), atom.v.y(), atom.v.z());
        fprintf(outfile, "\n");
    }
}

