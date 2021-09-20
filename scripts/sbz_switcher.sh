#!/bin/bash

n=$(aplay -l | grep -E -o '\[.*,' | sed -e 's/^.//' -e 's/..$//' | awk '!a[$0]++' | wc -l)
sbz_card=0;

# Getting Sound Blaster (HDA Creative) card ID.

for ((i=1; i<=$n; i++)); do
	card=$(aplay -l | grep -E -o '\[.*,' | sed -e 's/^.//' -e 's/..$//' | awk '!a[$0]++' | sed -n "$i"p)
	
	if [ "$card" == "HDA Creative" ]
	then
		sbz_card=$((i - 1))
	fi
	
done


# Getting Output Select (Headphones or Speakers) value.
# numid=36 ----> Output Select
# Type "amixer -c $sbz_card contents" to see IDs and other info.
output=$(amixer -c $sbz_card cget numid=36 | grep -E -o 'values=[0-9]$')

# Switch output
# amixer -c $sbz_card cset numid=36 $(( ($output + 1) % 2 ))

# output = 0 ----> Speakers
# output = 1 ----> Headphones 
if [ $output == "values=0" ]; then
	amixer sset 'Master' 14% > /dev/null 2>&1
	amixer -c $sbz_card cset numid=36 1 > /dev/null 2>&1
	echo "Switched to Headphones"
elif [ $output == "values=1" ]; then
	amixer sset 'Master' 68% > /dev/null 2>&1
	amixer -c $sbz_card cset numid=36 0 > /dev/null 2>&1
	echo "Switched to Speakers"
fi



