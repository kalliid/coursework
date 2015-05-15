nx = 60; % Number of p-values
N = 100;  % Number of experiments per p-value
Lx = 200; % Width of perc matrix
Ly = 200; % Height of perc matrix

pc = 0.59275;
dp = (1-pc)/(nx-1);
p = linspace(pc+dp, 1, nx); % p-values


Ni = zeros(nx, 1); % Number of spanning clusters at given p-value
Mi = zeros(nx, 1); % Mass of spanning cluster at given p-value

for i = 1:N
    i;
    
    % Generate random matrix
    z = rand(Lx, Ly);

    for ip = 1:nx

        % Check random matrix against p-value
        m = z < p(ip);

        % Label all clusters and extract their areas, bboxes
        [lw, num] = bwlabel(m, 4);
        s = regionprops(lw, 'BoundingBox');
        bbox = cat(1, s.BoundingBox);
        s = regionprops(lw, 'Area');
        area = cat(1, s.Area);

        % Find all spanning clusters
        jx = find(bbox(:,3) == Lx);
        jy = find(bbox(:,4) == Ly);
        j = union(jx, jy);

        j;
        
        % Tabulate results
        if length(j) > 0;
            Ni(ip) = Ni(ip) + 1;

            for jj = 1:length(j)
                Mi(ip) = Mi(ip) + area(j(jj));
            end
        end       
    end
end


Pi = Ni/N;
Mi = Mi/N/Lx/Ly;

plot(p, Mi)

y = log(Mi)
x = log(p - pc).'


beta = polyfit(x, y, 1)



