#!/usr/bin/env python

#Mapper 2

import sys
import operator
import re

prev_line=""
for line in sys.stdin:
	data=line.strip().split("\t")

	meme=data[0]

	occrs=data[1].split("|")

	titles=set(occr.split(",")[0] for occr in occrs)

	if len(titles)<2:
		continue

	for occr in occrs:
		title,index=occr.split(",")

		output_line=title+"\t"+meme+"="+occr
		if output_line==prev_line:
			continue
		print output_line
		prev_line=output_line
