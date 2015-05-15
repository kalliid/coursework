nx = 60;
N = 10;
L = 100;

p = linspace(0.4, 1, nx);
Ni = zeros(nx, 1);

for i = 1:N;
    z = rand(L, L);
    for ip = 1:nx;
        m = z < p(ip);
        [lw, num] = bwlabel(m,4);
        s = regionprops(lw, 'BoundingBox');
        bbox = cat(1, s.BoundingBox);
        maxsize = max(max(bbox(:,[3 4])));
        if (maxsize == L)
            Ni(ip) = Ni(ip) + 1;
        end
    end
end

Pi = Ni/i
plot(p, Pi)


