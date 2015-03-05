#ifndef VEC3_H
#define VEC3_H

#include <iostream>
class vec3
{
private:
    float m_vec[3];
public:
    // Assignment
    vec3();
    vec3(float x, float y, float z);

    // Inline
    inline float x() const { return m_vec[0]; }
    inline float y() const { return m_vec[1]; }
    inline float z() const { return m_vec[2]; }
    inline float &operator[](int index) { return m_vec[index]; }
    inline float operator[](int index) const { return m_vec[index]; }

    // Vector arithmetic operators
    vec3 operator +(vec3 rhs);
    vec3 operator -(vec3 rhs);
    vec3 operator *(vec3 rhs);
    vec3 operator /(vec3 rhs);

    // Scalar arithmetic operators
    vec3 operator +(float scalar);
    vec3 operator -(float scalar);
    vec3 operator *(float scalar);
    vec3 operator /(float scalar);

    // Assignment operators
    vec3 set(float x, float y, float z);
    vec3 operator +=(vec3 rhs);
    vec3 operator -=(vec3 rhs);
    vec3 operator *=(vec3 rhs);
    vec3 operator /=(vec3 rhs);
    vec3 operator +=(float scalar);
    vec3 operator -=(float scalar);
    vec3 operator *=(float scalar);
    vec3 operator /=(float scalar);

private:
    // Printing
    friend std::ostream& operator<<(std::ostream&stream, vec3 &vec);
};

#endif // VEC3_H
