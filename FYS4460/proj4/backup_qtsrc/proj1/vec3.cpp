#include <cmath>
#include "vec3.h"

// Assignment
vec3::vec3() {
    set(0, 0, 0);
}

vec3::vec3(float x, float y, float z) {
    set(x, y, z);
}

// Vector arithmetic operators
vec3 vec3::operator+(vec3 rhs) {
    return vec3( m_vec[0] + rhs.x(),
                 m_vec[1] + rhs.y(),
                 m_vec[2] + rhs.z());
}

vec3 vec3::operator-(vec3 rhs) {
    return vec3( m_vec[0] - rhs.x(),
                 m_vec[1] - rhs.y(),
                 m_vec[2] - rhs.z());
}

vec3 vec3::operator*(vec3 rhs) {
    return vec3( m_vec[0] * rhs.x(),
                 m_vec[1] * rhs.y(),
                 m_vec[2] * rhs.z());
}

// Scalar arithmetic operators
vec3 vec3::operator+(float scalar) {
    return vec3(m_vec[0] + scalar,
                m_vec[1] + scalar,
                m_vec[2] + scalar);
}

vec3 vec3::operator-(float scalar) {
    return vec3(m_vec[0] - scalar,
                m_vec[1] - scalar,
                m_vec[2] - scalar);
}

vec3 vec3::operator*(float scalar) {
    return vec3(m_vec[0] * scalar,
                m_vec[1] * scalar,
                m_vec[2] * scalar);
}

vec3 vec3::operator/(float scalar) {
    return vec3(m_vec[0] / scalar,
                m_vec[1] / scalar,
                m_vec[2] / scalar);
}

// Assignment operators
vec3 vec3::set(float x, float y, float z) {
    m_vec[0] = x;
    m_vec[1] = y;
    m_vec[2] = z;
    return *this;
}

vec3 vec3::operator +=(vec3 rhs) {
    m_vec[0] += rhs.x();
    m_vec[1] += rhs.y();
    m_vec[2] += rhs.z();
    return *this;
}

vec3 vec3::operator -=(vec3 rhs) {
    m_vec[0] -= rhs.x();
    m_vec[1] -= rhs.y();
    m_vec[2] -= rhs.z();
    return *this;
}

vec3 vec3::operator *=(vec3 rhs) {
    m_vec[0] *= rhs.x();
    m_vec[1] *= rhs.y();
    m_vec[2] *= rhs.z();
    return *this;
}

vec3 vec3::operator /=(vec3 rhs) {
    m_vec[0] /= rhs.x();
    m_vec[1] /= rhs.y();
    m_vec[2] /= rhs.z();
    return *this;
}

vec3 vec3::operator +=(float scalar) {
    m_vec[0] += scalar;
    m_vec[1] += scalar;
    m_vec[2] += scalar;
    return *this;
}

vec3 vec3::operator -=(float scalar) {
    m_vec[0] -= scalar;
    m_vec[1] -= scalar;
    m_vec[2] -= scalar;
    return *this;
}

vec3 vec3::operator *=(float scalar) {
    m_vec[0] *= scalar;
    m_vec[1] *= scalar;
    m_vec[2] *= scalar;
    return *this;
}

vec3 vec3::operator /=(float scalar) {
    m_vec[0] /= scalar;
    m_vec[1] /= scalar;
    m_vec[2] /= scalar;
    return *this;
}

std::ostream& operator<<(std::ostream &stream, vec3 &vec) {
    return stream << "[" << vec.x() << ", " << vec.y() << ", " << vec.z() << "]";
}
