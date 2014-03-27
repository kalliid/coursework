#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <mpi.h>

// These two functions come from the simplejpeg library
void import_JPEG_file(const char *filename, unsigned char **image_chars,
        int *image_height, int *image_width, int *num_components);

void export_JPEG_file(const char *filename, unsigned char *image_chars,
        int image_height, int image_width, int num_components, int quality);

typedef struct
{
    float** image_data;
    float* storage;     // used for contiguous storage
    int m;
    int n;
} image;

void allocate_image(image *u, int m, int n);
void deallocate_image(image *u);
void convert_jpeg_to_image(const unsigned char* image_chars, image *u);
void convert_image_to_jpeg(const image *u, unsigned char* image_chars);
void iso_diffusion_denoising(image *u, image *u_bar, float kappa);

int main (int argc, char *argv[])
{
    int m, n, c;
    int start, avrg, rest, rows, extra, total, counter, over, under;
    int my_rank,  worker, num_procs, num_workers;
    int iter, iters;
    float kappa;
    image u, u_bar;
    unsigned char *image_chars, *my_image_chars;
    char *infile, *outfile;

    int tag = 1;
    MPI_Status status;

    if (argc != 5) {
        printf("\nMissing paramters! Usage:\n");
        printf("./serial_main number_of_iterations kappa_value infile outfile\n\n");
        return 1;
    }

    MPI_Init(&argc, &argv);
    MPI_Comm_rank (MPI_COMM_WORLD, &my_rank);
    MPI_Comm_size (MPI_COMM_WORLD, &num_procs);
    num_workers = num_procs - 1;

    if (num_procs < 3) {
        printf("This program must be run with at least 3 processes. Exiting.\n");
        return 1;
    }

    iters = atoi(argv[1]);
    kappa = atof(argv[2]);
    infile  = argv[3];
    outfile = argv[4];

    if (my_rank == 0) {
        import_JPEG_file(infile, &image_chars, &m, &n, &c);
    }

    MPI_Bcast(&m, 1, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);

    avrg = m/num_workers;
    rest = m % num_workers;
    
    /* MASTER PROCESS */
    if (my_rank == 0) {
        /* DISTRIBUTE WORKLOAD */
        counter = 0;
        for (worker=1; worker<=num_workers; worker++) {
            rows = (worker <= rest) ? avrg+1 : avrg;
            extra = (worker==1 || worker==num_workers) ? 1 : 2;
            total = rows + extra;

            MPI_Send(&total, 1, MPI_INT, worker, tag, MPI_COMM_WORLD);
            MPI_Send(&image_chars[counter], total*n, 
                MPI_UNSIGNED_CHAR, worker, tag, MPI_COMM_WORLD);

            counter = counter + (total - 2)*n;
        }
        
        /* GATHER RESULTS */
        counter = 0;
        for (worker=1; worker<=num_workers; worker++) {
            rows = (worker <= rest) ? avrg+1 : avrg;
            
            MPI_Recv(&image_chars[counter], rows*n, MPI_UNSIGNED_CHAR, worker,
                        tag, MPI_COMM_WORLD, &status);

            counter = counter + rows*n;
        }

        /* WRITE RESULTS TO FILE */
        export_JPEG_file(outfile, image_chars, m, n, c, 75);

        free(image_chars);
    }


    /* WORKER PROCESS */
    else {
        /* SETUP */

        MPI_Recv(&total, 1, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);

        allocate_image(&u, total, n);
        allocate_image(&u_bar, total, n);
        my_image_chars = (unsigned char*)malloc(total*n*sizeof(unsigned char));

        MPI_Recv(&my_image_chars[0], total*n, 
            MPI_UNSIGNED_CHAR, 0, tag, MPI_COMM_WORLD, &status);

        convert_jpeg_to_image(my_image_chars, &u);

        /* ISO DIFFUSION ITERATIONS */
        for (iter=0; iter<iters; iter++) {
            iso_diffusion_denoising(&u, &u_bar, kappa);

            // Communicate boundaries

            over = (my_rank == 1) ? 0 : my_rank - 1;
            under = (my_rank == num_workers) ? 0 : my_rank + 1;

            if (over != 0)
                MPI_Sendrecv(&u.image_data[1][0], n, MPI_FLOAT, over, tag,
                             &u.image_data[0][0], n, MPI_FLOAT, over, tag,
                                MPI_COMM_WORLD, &status);

            if (under != 0)
                MPI_Sendrecv(&u.image_data[total-2][0], n,MPI_FLOAT,under,tag,
                             &u.image_data[total-1][0], n, MPI_FLOAT,under,tag,
                                    MPI_COMM_WORLD, &status);
        }

        /* RETURN RESULTS */
        convert_image_to_jpeg (&u, my_image_chars);

        deallocate_image(&u);
        deallocate_image(&u_bar);

        start = (under != 0) ? n : 0;
        rows = (under == 0 || over == 0) ? total-1 : total-2;
        
        MPI_Send(&my_image_chars[start], rows*n, MPI_UNSIGNED_CHAR, 0,
                    tag, MPI_COMM_WORLD);

        free(my_image_chars);
    }
        
    MPI_Finalize ();
    return 0;
}

void allocate_image(image *u, int m, int n)
{
    int i;
    u->m = m;
    u->n = n;
    u->storage = (float*)malloc(m*n*sizeof(float)); // for contiguous storage
    u->image_data = (float**)malloc(m*sizeof(float*));
    for (i=0; i<m; i++)
        u->image_data[i] = &(u->storage[i*n]);
}

void deallocate_image(image *u) 
{
    free(u->storage);
    free(u->image_data);
}

void convert_jpeg_to_image(const unsigned char* image_chars, image *u)
{
    // Converts an array of image chars into an image struct
    int i, j;
    int m = u->m;
    int n = u->n;
    for (i=0; i<m; i++)
        for (j=0; j<n; j++)
            u->image_data[i][j] = (float) image_chars[i*n+j];
}

void convert_image_to_jpeg(const image *u, unsigned char* image_chars)
{
    // Converts an image struct into an array of image chars
    int i, j;
    int m = u->m;
    int n = u->n;
    for (i=0; i<m; i++)
        for (j=0; j<n; j++)
            image_chars[i*n+j] = (unsigned char) u->image_data[i][j];
}

void iso_diffusion_denoising(image *u, image *u_bar, float kappa){
    // Does a single iteration of iso diffusion denoising
    int i, j;
    int m = u->m;
    int n = u->n;

    for (i=1; i<m-1; i++)
        for (j=1; j<n-1; j++)
            u_bar->image_data[i][j] = u->image_data[i][j] 
                + kappa*(u->image_data[i+1][j] + u->image_data[i][j+1]
                + u->image_data[i-1][j] + u->image_data[i][j-1]
                                         - 4*u->image_data[i][j]);
    
    for (i=1; i<m-1; i++)
        for (j=1; j<n-1; j++)
            u->image_data[i][j] = u_bar->image_data[i][j];    
}
