#!/usr/bin/env python

#Reducer1

import sys
import operator
import re

lower_bound=5
upper_bound=300000

def printOutput(prev_phrase, output):
	if len(output)>lower_bound and len(output)<upper_bound:
		print prev_phrase+"\t"+"|".join(output)


prev_phrase=""
output=[]
cnt=0

skip_flag=False
for line in sys.stdin:
	data=line.strip().split("\t")
	phrase=data[0]
	if prev_phrase!=phrase and len(output)>0:
		if skip_flag==False:
			printOutput(prev_phrase,output)
		skip_flag=False
		output=[]
		cnt=0
		
	if skip_flag==False:
		output.append(data[1])

	prev_phrase=phrase
	cnt+=1
	if cnt>upper_bound:
		output=[]
		skip_flag=True

if skip_flag==False:
	printOutput(prev_phrase,output)
