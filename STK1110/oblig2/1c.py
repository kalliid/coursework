import numpy as np

m = np.array([36.1, 36.3, 36.4, 36.6, 36.6, 36.6, 36.7, 37.0, 37.1])
k = np.array([36.6, 36.7, 36.8, 36.8, 36.8, 37.0, 37.1, 37.3, 37.4])

m_avg = sum(m)/len(m)
k_avg = sum(k)/len(k)

S2_m = sum((m - m_avg)**2)/(len(m)-1)
S2_k = sum((k - k_avg)**2)/(len(k)-1)

S2_p = 0.5*S2_m + 0.5*S2_k

print k_avg - m_avg

print S2_k/S2_m

print S2_m
print S2_k
print S2_p

se1 = np.sqrt(S2_m)/3
se2 = np.sqrt(S2_k)/3

#se1 = np.sqrt(S2_p)/3
#se2 = np.sqrt(S2_p)/3

n = 9
m = 9

print (m_avg - k_avg)/np.sqrt(S2_p*(1/9.+1/9.))
print (se1**2 + se2**2)**2 / ((se1**4/(m-1)) + (se2**4/(n-1)))

print (k_avg - m_avg)
print 2.12*np.sqrt(S2_p*(1./n + 1./m))

print (k_avg - m_avg)/(np.sqrt(S2_m/9 + S2_k/9))

print (k_avg - m_avg) - 2.131*np.sqrt(S2_m/n + S2_k/m)
print (k_avg - m_avg) + 2.131*np.sqrt(S2_m/n + S2_k/m)