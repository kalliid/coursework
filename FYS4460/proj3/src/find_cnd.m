M = 30; % Number of experiments per p-value
L = 400;

pc = 0.59275;
p = pc - (0.1:-0.01:0.01);

nbins = 100;
a = 0;
b = log10(L*L);
starts = unique(round(logspace(a,b,nbins)));
centers = 0.5*(starts(1:end-1) + starts(2:end));
ds = diff(starts);

for ip = 1:length(p)
    clusters = [];
    bins = zeros(length(ds), 1);
    for ie = 1:M
        ie
        z = rand(L, L);
        m = z < p(ip);
        [lw, num] = bwlabel(m, 4);

        s = regionprops(lw, 'BoundingBox');
        bbox = cat(1, s.BoundingBox);
        s = regionprops(lw, 'Area');
        area = cat(1, s.Area);

        % Find all non-spanning clusters
        non_spanning_clusters = intersect(find(bbox(:,3) < L), find(bbox(:,4) < L));
        
        for ic = non_spanning_clusters'
            clusters(end+1) = area(ic);
        end
    end
    
    for c = clusters
        for si = 1:length(ds)
            if c < starts(si+1)
                bins(si) = bins(si) + 1;
                break
            end
        end
    end
   
    nsl = bins'./(M*L*L*ds);
    loglog(centers, nsl)
    hold('on')
end






%
%    
%
%z = rand(L, L);
%m = z < p;
%
%s = regionprops(lw, 'Area')
%area = cat(1, s.Area);
%
%
%
%
%
%
%N = 100; % Number of experiments per p-value
%
%pc = 0.59275;
%prange = 0.5:0.01:pc;
%L = 400;
%
%a = log10(1);
%b = log10(L*L);
%starts = logspace(a, b);
%global_bins = zeros(50, length(prange));
%
%for ip = 1:length(prange)
%    for i = 1:N
%        i
%        clusters = [];
%        bins = zeros(50, 1);
%
%        % Generate random matrix
%        z = rand(L, L);
%
%        % Check random matrix against p-value
%        m = z < prange(ip);
%
%        % Label all clusters and extract their areas, bboxes
%        [lw, num] = bwlabel(m, 4);
%        s = regionprops(lw, 'BoundingBox');
%        bbox = cat(1, s.BoundingBox);
%        s = regionprops(lw, 'Area');
%        area = cat(1, s.Area);
%
%        % Find all non-spanning clusters
%        jx = find(bbox(:,3) < L);
%        jy = find(bbox(:,4) < L);
%        j = intersect(jx, jy);
%
%        % Tabulate results
%        if length(j) > 0;
%            for jj = 1:length(j)
%                clusters(end+1) = area(j(jj));
%            end
%        end
%
%        for s = clusters
%            for i = 1:49
%                if  s < starts(i+1);
%                    bins(i) = bins(i) + 1;
%                    break
%                end
%            end
%        end
%
%        bins = bins/sum(bins);
%        global_bins(:, ip) = global_bins(:, ip) + bins;
%    end
%    global_bins(:, ip) = global_bins(:, ip)/N;
%    loglog(starts, global_bins(:, ip))
%    if ip==1
%        hold('on')
%    end
%end
%
%%hold('on');
%%legend(['0.50', '0.51', '0.52', '0.53', '0.54', '0.55', '0.56', '0.57', '0.58', '0.59']);
%%xlabel('log10(s)');
%%ylabel('log10(n(s,p))');
%
%





