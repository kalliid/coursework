N = 1e6; % num of random points
Z = rand(N, 1).^(-1);

n = 1001; % num of bins
P = zeros(n, 1);
z = logspace(0,10,n)';

for i=1:n
    P(i) = sum(Z < z(i));
end

P = P/N;

figure();
%plot(log10(z), P);


x = log10(z);
y = log10(gradient(P));

plot(log10(z), gradient(P))

hold('on')
%plot(x(1:100), y(1:100))
%polyfit(x(1:100), y(1:100),1)
%plot(x(1:100), -2-0.5*x(1:100))

%polyfit(log10(z), log10(gradient(P)), 1)


%alphaplusone = polyfit(log10(starts),log10(1-bins),1)



% % better attempt
% n = 51;
% bins = zeros(n,1);
% binStarts = logspace(0,10,n+1);
% for i=1:length(bins)
%     tester = (z>binStarts(i)).*(z<binStarts(i+1));
%     bins(i) = sum(tester);
%     binSize = (binStarts(i+1)-binStarts(i));
%     bins(i) = bins(i)/binSize;
%     
% end  
% bins = bins/N;
% starts = log10(binStarts(1:length(bins)));
% log10bins = log10(bins)';
% plot(starts,bins)
% figure()
% plot(starts,log10bins)
% alpha = polyfit(starts,log10bins,1)


% culumative distribution
% n = 1001;
% bins = zeros(n,1);
% starts = logspace(0,10,n)';
% 
% for i=1:n
%     bins(i) = sum(z<starts(i));
%     
% end
% 
% bins = bins/N;
% 
% figure()
% plot(log10(starts),bins)
% 
% figure()
% plot(log10(starts),log10(1-bins))
% alphaplusone = polyfit(log10(starts),log10(1-bins),1)
% 
% 
% 
% 
% density = zeros(n-1,1);
% density(:) = bins(2:n) - bins(1:n-1);
% 
% binStarts = binStarts(1:n-1)';
% density = density./binStarts;
% figure()
% plot(log10(binStarts),density);
% alpha = polyfit(log10(binStarts),log10(density),1)