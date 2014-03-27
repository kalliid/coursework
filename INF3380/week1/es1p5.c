#include <string.h>
#include <stdio.h>
#include <stdlib.h>


int main()
{
    const char* filename = "temps.dat";
    const char* delimiter = " ";

    char line[128];
    char *time, *temp;
    FILE *infile = fopen(filename, "rt");
    
    int i=0, j;
    double temptemps[1024];

    while (fgets(line, sizeof(line), infile) != NULL)
    {
        time = strtok(line, delimiter);
        temptemps[i++] = atof(strtok(NULL, delimiter));
    }
    fclose(infile);

    double *temps = (double *)malloc(i*sizeof(double));
    for (j=0; j<i; j++)
        temps[j] = temptemps[j];

    return 0;
}


