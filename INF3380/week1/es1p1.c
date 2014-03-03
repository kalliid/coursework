#include <stdio.h>
#include <math.h>

int main()
{
    int i;
    int N = 1000;
    double s = 0;
        for (i=0; i<N; i++)
            s = s + pow(-1, i)*pow(0.5, 2*i);   

    printf("%f\n", s);
}


