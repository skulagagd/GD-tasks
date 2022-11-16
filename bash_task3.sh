#!/bin/bash

for((INDEX=1;INDEX<=100;INDEX++)); do
    if [ "$(($INDEX % 15))" -eq "0" ]; then
        echo "FizzBuzz"
    elif [ "$(($INDEX % 5))" -eq "0" ]; then
        echo "Buzz"
    elif [ "$(($INDEX % 3))" -eq "0" ]; then
        echo "Fizz"
    else
        echo "$INDEX"
    fi
done
