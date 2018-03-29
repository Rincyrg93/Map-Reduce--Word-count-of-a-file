#Rincy Raju George(Big- Data problem)- Reducer code to display the number of times the word occurs in each file.
#!/usr/bin/env python 
import sys
import os
import re

if __name__== "__main__":
	current_word=None
	
	dictFiles={}
	count=0
	total=0
	for line in sys.stdin:
		
		w,fileDesc= line.strip().split("\t")
		fname,fcount=fileDesc.split(":")
		fname=fname.strip()
		fcount=int(fcount)
		
		if w == current_word:
			total+=fcount
			dictFiles[fname]=total
	
		else:
			if current_word is not None:
				sys.stdout.write("{0}\t{1}\n".format(current_word,dictFiles))
					
			current_word=w
			dictFiles={}
			total=fcount
			dictFiles[fname]=total
						
	if current_word:
		sys.stdout.write("{0}\t{1}\n".format(current_word,dictFiles))

			
