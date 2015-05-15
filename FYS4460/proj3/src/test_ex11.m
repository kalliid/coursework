M = 100; % Number of experiments per p-value
L = 2;

p = (0:0.01:1);

N = zeros(length(p), 1);
P = zeros(length(p), 1);

for i=1:M
    i
    z = rand(L, L);
    for ip = 1:length(p)
        m = z < p(ip);
        [lw, num] = bwlabel(m, 4);

        s = regionprops(lw, 'BoundingBox');
        bbox = cat(1, s.BoundingBox);
        s = regionprops(lw, 'Area');
        area = cat(1, s.Area);

        if size(bbox) ~= [0,0]
            jx = find(bbox(:,3) == 2);
            jy = find(bbox(:,4) == 2);
            j = union(jx, jy);
            if j>0
                N(ip) = N(ip) + 1;
                P(ip) = P(ip) + area(1);
            end
        end
    end
end

plot(p, P/(L*L*M))
