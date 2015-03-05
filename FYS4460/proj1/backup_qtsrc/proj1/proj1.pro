TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp \
    initialize.cpp \
    vec3.cpp \
    io.cpp \
    integrator.cpp \
    system.cpp

HEADERS += \
    argon_lattice.h \
    vec3.h \
    integrator.h \
    system.h \
    io.h

release {
    DEFINES += ARMA_NO_DEBUG
    QMAKE_CXXFLAGS_RELEASE -= -O2
    QMAKE_CXXFLAGS_RELEASE += -O3
}

COMMON_CXXFLAGS = -std=c++0x
QMAKE_CXXFLAGS += $$COMMON_CXXFLAGS
QMAKE_CXXFLAGS_RELEASE += $$COMMON_CXXFLAGS
QMAKE_CXXFLAGS_DEBUG += $$COMMON_CXXFLAGS
