from vec3d import Vec3D as Vec3D_base

class Vec3D(Vec3D_base):
    '''Extension of the Vec3D class created in week 6'''
    
    def __add__(self, other):
        '''Add should now also handle scalars'''   
        if isinstance(other, Vec3D):
            # Normal vector addition
            return Vec3D_base.__add__(self, other)

        elif isinstance(other, (int, float)):
            # Add the scalar to each component
            x, y, z = self.coordinates
            return Vec3D(x+other, y+other, z+other)

    def __radd__(self, other):
        '''Addition is commutative, so the reverse addition
        can simply call the Vec3D addition method.'''
        return self.__add__(other)

    def __sub__(self, other):
        '''Sub should now also handle scalars'''
        if isinstance(other, Vec3D):
            # Normal vector subtraction
            return Vec3D_base.__sub__(self, other)
        elif isinstance(other, (int, float)):
            # Subtract the scalar from each component
            x, y, z = self.coordinates
            return Vec3D(x-other, y-other, z-other)

    def __rsub__(self, other):
        '''Subtraction is not commutative, so we define
         the reverse subtraction method explicitly.'''
        x, y, z = self.coordinates
        return (other-x, other-y, other-z)

    def __mul__(self, other):
        '''Should handle multiplication by scalar'''
        if isinstance(other, Vec3D):
            # Normal dot product
            return Vec3D_base.__mul__(self, other)
        elif isinstance(other, (int, float)):
            # Multiply each component by the scalar
            x, y, z = self.coordinates
            return Vec3D(x*other, y*other, z*other)

    def __rmul__(self, other):
        '''Multiplication is commutative'''
        return self.__mul__(other)

    def __div__(self, other):
        if isinstance(other, Vec3D):
            raise TypeError('Vector divided by vector is not defined')
        elif isinstance(other, (int, float)):
            # Divide each component by the scalar
            x, y, z = self.coordinates
            c = float(other)
            return Vec3D(x/c, y/c, z/c)

    def __rdiv__(self, other):
        raise TypeError('Scalar divided by vector is not defined')
