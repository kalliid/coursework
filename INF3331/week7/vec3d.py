class Vec3D:
    '''Class for representing real 3D vectors'''

    def __init__(self, x, y, z):
        '''Constructor, takes the vectors coordinates'''
        self.coordinates = [x, y, z]
        
    def __add__(self, other):
        '''Adds two vectors together, defining a new vector'''
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = other.coordinates
        return Vec3D(x1+x2, y1+y2, z1+z2)

    def __sub__(self, other):
        '''Subtracts the second vector from the first, defining a third'''
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = other.coordinates
        return Vec3D(x1-x2, y1-y2, z1-z2)
        
    def __mul__(self, other):
        '''Vector scalar product between two vectors, returns a scalar'''
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = other.coordinates
        return x1*x2 + y1*y2 + z1*z2

    def __pow__(self, other):
        '''Vector cross product between two vectors, returns a Vec3D'''
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = other.coordinates
        x = y1*z2 - y2*z1
        y = x2*z1 - x1*z2
        z = x1*y2 - x2*z1
        return Vec3D(x, y, z)

    def __getitem__(self, key):
        '''Allows subscripting of the vector'''
        return self.coordinates[key]

    def __setitem__(self, key, value):
        '''Allows assignment through subscripting'''
        self.coordinates[key] = value

    def __str__(self):
        '''Informal string representation of the vector'''
        x, y, z = self.coordinates
        return '(%g, %g, %g)' % (x, y, z)

    def __repr__(self):
        '''Formal string representation of the object'''
        x, y, z = self.coordinates
        return 'Vec3D(%g, %g, %g)' % (x, y, z)

    def len(self):
        '''Returns the eucledian norm'''
        x, y, z = self.coordinates
        return (x**2 + y**2 + z**2)**(1./2)
