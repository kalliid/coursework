x = rand(1);

if (x<0.6)
    disp('You loose!')
elseif (0.6 <= x) & (x < 0.99)
    disp('You win!')
else 
    disp('You win the Jacpot!')
end