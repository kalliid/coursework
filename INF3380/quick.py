a = [3,2,1,5,8,4,3,7]

def swap(i,j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

x = a[0]
s = 0
for i in range(1,8):
    if a[i] <= x:
        s = s+1
        print s, i
        swap(s,i)
print 0, s
swap(0,s)

print a

