#!/bin/bash

while getopts "i:o:vsrlu" OPTION; do
    case "$OPTION" in
        i)
            INPUT="$OPTARG"
            ;;
        o)
            OUTPUT="$OPTARG"
            ;;
        v)
            tr "[:lower:][:upper:]" "[:upper:][:lower:]" < "$INPUT" > "$OUTPUT"    
            ;;
        s)  
            AWORD="$6"
            BWORD="$7"
            sed "s/$AWORD/$BWORD/g" < "$INPUT" > "$OUTPUT"
            ;;
        r)
            tail -r "$INPUT" > "$OUTPUT"
            ;;
        l)
            tr "[:upper:]" "[:lower:]" < "$INPUT" > "$OUTPUT"
            ;;
        u)
            tr "[:lower:]" "[:upper:]" < "$INPUT" > "$OUTPUT"
            ;;
        *)
            echo 'Wrong flag, should be: $0 -i <input-file> -o <output-file> [ -v | -s <a_word> <b_word> | -r | -l | -u ]'
            exit "1"
            ;;
    esac
done