class SparseVec:
    '''Class for representing a sparse vector of a specified size'''

    def __init__(self, size):
        self.size = size
        self.elements = {k:0 for k in range(size)}
        
    def __getitem__(self, key):
        # Need to explicitily check the index
        if key > (self.size - 1):
            raise IndexError('index out of range')
        return self.elements[key]

    def __setitem__(self, key, value):
        # Need to explicitily check the index
        if key > (self.size - 1):
            raise IndexError('index out of range')
        self.elements[key] = value

    def __str__(self):
        s = ['[%d]=%g' % (k, self.elements[k]) for k in self.elements.keys()]
        return ' '.join(s)

    def __len__(self):
        return self.size
        
    def __add__(self, other):
        # Adds to sparse vectors together, defining a third.
        new = SparseVec(max(self.size, other.size))
        for ai, i in self:
            new[i] += ai
        for ai, i in other:
            new[i] += ai 
        return new  

    def __iter__(self):
        # Returns iterator
        self.k = 0 
        return self

    def nonzeros(self):
        # Returns the non-zero elements as a dictionary
        d = self.elements
        return {k:d[k] for k in d.keys() if d[k]}

    def next(self):
        # Increment iterator object by one, raise stop when done
        k = self.k
        self.k += 1
        if k == self.size:
            raise StopIteration
        else:
            return self.elements[k], k