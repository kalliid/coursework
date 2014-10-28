% Generate a matrix with random elements
nx = 6; ny = 4;
A = rand(6,4);

% Remove every element smaller than 0.5
for i=1:nx
	for j=1:ny
		if (A(i,j) < 0.5)
			A(i,j) = 0;
		end
	end
end