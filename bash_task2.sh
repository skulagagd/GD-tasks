#!/bin/bash

#functions declarations
subtract() {
    RESULT=$1
    shift
    for NUMBER in $@; do
        RESULT=$((RESULT - NUMBER))
    done
    echo $RESULT
}

add() {
    for NUMBER in $@; do
        RESULT=$((RESULT + NUMBER))
    done
    echo $RESULT
}

multiply() {
    RESULT=1
    for NUMBER in $@; do
        RESULT=$((RESULT * NUMBER))
    done
    echo $RESULT
}

modulo() {
    if [ -z "$2" ] || [ -n "$3" ]; then
        exit "3"
    fi
    echo $(($1 % $2)) 
}

#main program
while getopts "o:n:d" OPTION; do
    case "$OPTION" in
        o)
            OPERATION="$OPTARG"
            ;;
        n)
            NUMBERS="$OPTARG"
            ;;
        d)
            VIEWDISPLAY="TRUE"
            ;;
        *)
            echo 'Wrong flag, should be: $0 -o +/-/m/% -n "NUMBERS..." [-d]'
            exit "1"
            ;;
    esac
done

shift $((OPTIND-1))

case "$OPERATION" in
    -)
        RESULT=$(subtract $NUMBERS)
        ;;
    +)
        RESULT=$(add $NUMBERS)
        ;;
    m)
        RESULT=$(multiply $NUMBERS)
        ;;
    %)
        RESULT=$(modulo $NUMBERS)
        if [ "$?" -eq "3" ]; then
            echo "Invalid number of arguments for -n, should be 2 values"
            exit "3"
        fi
        ;;
    *)
        echo 'Wrong operation, should be: $0 -o +/-/m/% -n "NUMBERS..." [-d]'
        exit "2"
        ;;
esac

echo "Result: $RESULT"

if [ "$VIEWDISPLAY" == "TRUE" ]; then
    echo "User: $USER"
    echo "Script: $0"
    echo "Operation: $OPERATION"
    echo "Numbers: $NUMBERS"
fi