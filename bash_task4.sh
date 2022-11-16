#!/bin/bash

while getopts "s:i:o:" OPTION; do
    case $OPTION in
        s)
            ROT=$OPTARG
            ;;
        i)
            INPUT=$OPTARG
            ;;
        o)
            OUTPUT=$OPTARG
            ;;
        *)
            echo "Invalid options, should be $0 -s <-26,26> -i <input-file> -o <output-file>"
            exit 1
            ;;
    esac
done

if [ ! -f $INPUT ]; then
    echo "Input file doesn't exist"
    exit "2"
fi

if [ -e $OUTPUT ]; then
    echo "Output file exists"
    exit "3"
fi

if [ "$ROT" -lt "-26" ] || [ "$ROT" -gt "26" ]; then
    echo "Wrong value for shift argument, should be <-26,26>"
    exit "4"
fi

A="abcdefghijklmnopqrstuvwxyz"
B="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if [ "$ROT" -lt "0" ]; then
    ROT=$((26 + $ROT))
fi

sed "y/$A$B/${A:$ROT}${A::$ROT}${B:$ROT}${B::$ROT}/" ./$INPUT > "./$OUTPUT"