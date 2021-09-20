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

echo $sbz_card