#!/bin/bash

# Set default values
filename='input.i'
interval='[0,100]'
step='0.1'
integrator='ode15s'
b='1.0'
p='2.0'
r='1.0'
d='0.5'

# Read command-line args
for arg in $@; do
    shift
    if [ $arg = '-b' ]; then
        b=$1
    elif [ $arg = '-p' ]; then
        p=$1
    elif [ $arg = '-r' ]; then
        r=$1
    elif [ $arg = '-d' ]; then
        d=$1
    fi
done

filename='input.i'

cat > $filename <<EOF
set time interval = $interval
set time step = $step
set integrator = $integrator
set b = $b
set p = $p
set r = $r
set d = $d
EOF


# echo set time interval = $interval > $filename
# echo set time step = $step >> $filename
# echo set integrator = $integrator >> $filename
# echo set b = $b >> $filename 
# echo set p = $p >> $filename
# echo set r = $r >> $filename
# echo set d = $d >> $filename

# bash predator.sh<input.i