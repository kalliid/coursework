from pylab import *

infiles1 = ["../data/relfluct_nsh_Nc8_T800_tau15",
            "../data/relfluct_nsh_Nc8_T800_tau50",
            "../data/relfluct_nsh_Nc8_T800_tau150",
            "../data/relfluct_nsh_Nc8_T800_tau300"]

infiles2 = ["../data/relfluct_ber_Nc8_T800_tau15",
            "../data/relfluct_ber_Nc8_T800_tau50",
            "../data/relfluct_ber_Nc8_T800_tau150",
            "../data/relfluct_ber_Nc8_T800_tau300"]

infiles3 = ["../data/relfluct_and_Nc8_T800_tau15",
            "../data/relfluct_and_Nc8_T800_tau50",
            "../data/relfluct_and_Nc8_T800_tau150",
            "../data/relfluct_and_Nc8_T800_tau300"]

tau = [15, 50, 150, 300]

print "Theoretical: %e\n" % (2/(3.*2048))

print "Nose-hoover:"
for i in range(4):
    with open(infiles1[i], 'r') as infile:
        lines = infile.readlines()
        T = zeros(len(lines))
        for j in range(len(lines)):
            T[j] = lines[j].split()[-1]

    print "tau=%f*dt:\t %e" % (tau[i], var(T)/(average(T)**2))

print "\n Berendsen:"
for i in range(4):
    with open(infiles2[i], 'r') as infile:
        lines = infile.readlines()
        T = zeros(len(lines))
        for j in range(len(lines)):
            T[j] = lines[j].split()[-1]

    print "tau=%f*dt:\t %e" % (tau[i], var(T)/(average(T)**2))

print "\n Andersen:"
for i in range(4):
    with open(infiles3[i], 'r') as infile:
        lines = infile.readlines()
        T = zeros(len(lines))
        for j in range(len(lines)):
            T[j] = lines[j].split()[-1]

    print "tau=%f*dt:\t %e" % (tau[i], var(T)/(average(T)**2))
