from numpy import argmin

class PancakeHeap:
    def __init__(self, a):
        self.a = a
        self.n = len(a)

    def flip(self, i):
        b = self.a[0:i+1]
        b.reverse()
        self.a[0:i+1] = b

    def min(self, i, j):
        return argmin(self.a[i:j])

    def sort(self):
        n = self.n
        
        while (n > 0):
            i = n
            while (i > 0):
                if max(i,n+1) != n:
                    self.flip(n+1)
                    i = 0
                else:
                    i -= 1
            n -= 1

test = PancakeHeap([7,2,1,4,3,5])
test.sort()
print test.a
