from pylab import *

x1 = [1.2, 1.4, 1.6, 2.1, 2.6, 3.6, 5.6, 10.6, 15.6]
x2 = [1.2, 1.6, 2.1, 2.7, 3.6, 3.7, 5.6, 10.6]
y1 = [9.75, 9.93, 10.01, 10.02, 9.92, 9.65, 9.09, 7.6, 6.21]
y2 = [7.3, 7.73, 8.09, 8.64, 8.93, 9.04, 8.72, 7.69, 6.71]
y3 = [10.812528, 10.894176, 8.852976, 3.767472, 0.081648,  0.05832, 0.046656, 0.034992]
y4 = [10.637568, 10.940832, 11.279088, 11.465712, 10.55592, 10.26432, 1.423008, 0.151632]


plot(x1, y1, 'o-')
plot(x1, y2, 'o-')
plot(x2, y3, 'o-')
plot(x2, y4, 'o-')
xlabel('Tykkelse av PMMA (mm)')
ylabel('Total ladning (nC)')
legend(['Foton 6 MV', 'Foton 15 MV', 'Elektron 6 MeV', 'Elektron 12 MeV'])
grid()
savefig('dybdedose.pdf')
show()

x = [0, 5, 7, 8.7, 9, 10.5]
y = [1, 1.012207528, 0.8189216684, 0.2868769074, 0.2054933876, 0.0335707019]
plot(x,y, 'o-')
xlabel('Forflyttning av dosimeter (cm)')
ylabel('Relativ total ladning')
grid()
savefig('tverrscan.pdf')
show()
