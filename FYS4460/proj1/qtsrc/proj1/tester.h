#ifndef TESTER_H
#define TESTER_H

#include <random>
#include <algorithm>
#include <iostream>

using namespace std;

struct Foo {
    mt19937 gen {random_device{}()};
//    uniform_int_distribution<> dist1 {1, 20};
//    uniform_real_distribution<> dist2 {0.0, 100.0};

    normal_distribution<double> std_norm_dist{0.0, 1.0};


//    Foo() = default;
//    Foo(mt19937::result_type seed) : eng{seed} {}

    double bar() {
        return std_norm_dist(gen);
    }

    double baz() {
        return std_norm_dist(gen);
    }
};


#endif // TESTER_H
