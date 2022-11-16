#!/bin/bash

echo "Give n for fibonacchi"
read VALUE

fib () {
    A=0
    B=1
    N="$1"
    for((i=0;i<$N;i++)); do
        B="$(($A + $B))"
        A="$(($B - $A))"
    done
    echo "$A"
}

RESULT=$(fib $VALUE)
echo "Fn of $VALUE is $RESULT"