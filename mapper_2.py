#!/usr/bin/env python 
import sys
import os
import re
import string 

if __name__=='__main__':
	for line in sys.stdin:
		line=line.lower()
		p=string.punctuation
		d=string.digits
		tables=string.maketrans(p,len(p)*" ")
		text1=line.translate(tables)
		tables=string.maketrans(d,len(d)*" ")
		text1=text1.translate(tables)
		filename=os.getenv("map_input_file")
		filename=filename.split('/')[-1]
		w=text1.split()
		for word in w:
			sys.stdout.write("{0}\t{1}:1\n".format(word,filename))
