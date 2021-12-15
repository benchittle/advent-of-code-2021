#!/bin/bash

# Fun utitlity script to create a folder for the next day's code

# Get the highest day number so far
highest=0
for d in */ ; do
    num=${d: -3:2}          # Get the day number for the current directory
    if [ $num -gt $highest ] ; then
        highest=$num
    fi
done

# Determine the name of the directory for the next day
new=day$(printf "%02d" $((highest + 1)))/

# Create a new directory for the next day
mkdir $new
# Create a new Python file with some starter code
echo -e '\n\nwith open("sample.txt") as file:\n    data = file.read()\n\n' > $new/part1.py
# Create an empty file for part 2's code
touch $new/part2.py
# Create an empty file for the sample input
touch $new/sample.txt