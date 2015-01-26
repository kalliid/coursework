# Extract x and y coordinates
x = r[:,0]
y = r[:,1]

# Plot figure
plot(x,y)

# Prettify the plot
xlabel('Horizontal distance, [m]')
ylabel('Vertical distance, [m]')
title('Trajectory of a fired cannonball')
grid()
axis([0, 900, 0, 250])

# Makes the plot appear on the screen
show()