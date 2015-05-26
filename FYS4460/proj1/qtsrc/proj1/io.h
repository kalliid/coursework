#ifndef IO_H
#define IO_H

#include "system.h"

class Logger {
private:
    System* system;
    FILE* outfile;

public:
    Logger(System* system, const char filename[]);
    ~Logger();
    void write_header(char header[]);
    void write_current_state();

    static System resume_state(const char filename[]);
};


#endif // IO_H
