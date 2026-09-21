#! /bin/sh
# script to start ipp with problem and domain files
# with filepaths given in a file
# first arg is input file
# second arg is output file

#########################################################
# TODO:
# which sh : shell anpassen
# IPP=ipp/rifo richtiges Programm auswaehlen
#########################################################

# reset  separators
IFS=" "

#set the planer
IPP=./ipp
#IPP=rifo

echo >> $2
echo IPP >> $2

while read dom; do
    read prob
    echo Executing:
    echo "$IPP -o $dom -f $prob -z $2"
    csh << EOF 
    limit memoryuse 120000
    limit datasize 100000
    limit coredumpsize 0
    limit cputime 600
    $IPP -o $dom -f $prob -z $2
    exit

EOF
    
done < $1

