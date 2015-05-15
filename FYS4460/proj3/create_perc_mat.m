function [m] = create_perc_mat(p, Lx, Ly)

z = rand(Lx, Ly);
m = z < p;
