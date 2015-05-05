#ifndef VEC3_H
#define VEC3_H

#include <iostream>
class vec3
{
private:
    double m_vec[3];
public:
    // Assignment
    vec3();
    vec3(double x, double y, double z);

    // Inline
    inline double x() const { return m_vec[0]; }
    inline double y() const { return m_vec[1]; }
    inline double z() const { return m_vec[2]; }
    inline double &operator[](int index) { return m_vec[index]; }
    inline double operator[](int index) const { return m_vec[index]; }
    inline double length_squared() { return m_vec[0]*m_vec[0] + m_vec[1]*m_vec[1] + m_vec[2]*m_vec[2]; }

    // Vector arithmetic operators
    vec3 operator +(vec3 rhs);
    vec3 operator -(vec3 rhs);
    vec3 operator *(vec3 rhs);
    vec3 operator /(vec3 rhs);
    vec3 operator %(vec3 rhs);

    // Scalar arithmetic operators
    vec3 operator +(double scalar);
    vec3 operator -(double scalar);
    vec3 operator *(double scalar);
    vec3 operator /(double scalar);

    // Assignment operators
    vec3 set(double x, double y, double z);
    vec3 operator +=(vec3 rhs);
    vec3 operator -=(vec3 rhs);
    vec3 operator *=(vec3 rhs);
    vec3 operator /=(vec3 rhs);
    vec3 operator +=(double scalar);
    vec3 operator -=(double scalar);
    vec3 operator *=(double scalar);
    vec3 operator /=(double scalar);

    // Vector products
    double dot(vec3 &rhs);

    // Other
    double length();
    vec3 normalize();
    vec3 round();
    vec3 floor();
    double sum();


private:
    // Printing
    friend std::ostream& operator<<(std::ostream&stream, vec3 &vec);
};

#endif // VEC3_H
