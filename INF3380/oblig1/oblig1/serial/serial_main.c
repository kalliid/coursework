#include <string.h>
#include <stdlib.h>
#include <stdio.h>

// make use of two functions from the simplejpeg library
void import_JPEG_file(const char *filename, unsigned char **image_chars,
        int *image_height, int *image_width, int *num_components);

void export_JPEG_file(const char *filename, unsigned char *image_chars,
        int image_height, int image_width, int num_components, int quality);

typedef struct
{
    float** image_data;
    float* storage;     // contiguous storage
    int m;
    int n;
} image;

void allocate_image(image *u, int m, int n);
void deallocate_image(image *u);
void convert_jpeg_to_image(const unsigned char* image_chars, image *u);
void convert_image_to_jpeg(const image *u, unsigned char* image_chars);
void iso_diffusion_denoising(image *u, image *u_bar, float kappa, int iters);

int main (int argc, char *argv[])
{
    int m, n, c, iters;
    float kappa;
    image u, u_bar;
    unsigned char *image_chars;
    char *infile, *outfile;

    if (argc != 5) {
        printf("\nMissing paramters! Usage:\n");
        printf("./serial_main number_of_iterations kappa_value infile outfile\n\n");
    }

    iters = atoi(argv[1]);
    kappa = atof(argv[2]);
    infile  = argv[3];
    outfile = argv[4];

    import_JPEG_file(infile, &image_chars, &m, &n, &c);

    allocate_image (&u, m, n);
    allocate_image (&u_bar, m, n);

    convert_jpeg_to_image (image_chars, &u);

    iso_diffusion_denoising (&u, &u_bar, kappa, iters);

    convert_image_to_jpeg (&u, image_chars);
    export_JPEG_file(outfile, image_chars, m, n, c, 75);
    
    deallocate_image (&u);
    deallocate_image (&u_bar);
    return 0;
}

void allocate_image(image *u, int m, int n)
{
    int i;
    u->m = m;
    u->n = n;
    u->storage = (float*)malloc(m*n*sizeof(float));
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
    int i, j;
    int m = u->m;
    int n = u->n;
    for (i=0; i<m; i++)
        for (j=0; j<n; j++)
            u->image_data[i][j] = (float) image_chars[i*n+j];
}

void convert_image_to_jpeg(const image *u, unsigned char* image_chars)
{
    int i, j;
    int m = u->m;
    int n = u->n;
    for (i=0; i<m; i++)
        for (j=0; j<n; j++)
            image_chars[i*n+j] = (unsigned char) u->image_data[i][j];
}

void iso_diffusion_denoising(image *u, image *u_bar, float kappa, int iters){
    int iter, i, j;
    int m = u->m;
    int n = u->n;

    for (iter=0; iter<iters; iter++){
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
}

