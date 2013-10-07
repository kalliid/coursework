#!/usr/bin/env python
import sys, re

usage = 'Usage: %s infile word' % sys.argv[0]

# Try reading cmd-line arguments
try:
	infile = sys.argv[1]
	word = sys.argv[2]
except:
	print usage; sys.exit(1)

# Read in text as a single string
infile = open(infile, 'r')
text = "".join(infile.readlines())
infile.close()

# Read flags
b = '-b' in sys.argv # Respect word boundaries
i = '-i' in sys.argv # Ignore letter case

# Create expression and compile pattern
expr = r'\b'+word+r'\b' if b else word
pattern = re.compile(expr, re.I) if i else re.compile(expr)

# Find number of occurances
count = len(re.findall(pattern, text))

# Print results
b = 'word' if b else 'string'
i = ' (case insensitive)' if i else ''
print "Number of occurances of %s '%s'%s: %i" % (b, word, i, count)

'''
user$ python count_words.py football.txt ball
Number of occurances of string 'ball': 3
user$ python count_words.py football.txt goal -i
Number of occurances of string 'goal' (case insensitive): 3
user$ python count_words.py football.txt goal -i -b
Number of occurances of word 'goal' (case insensitive): 2
user$ python count_words.py football.txt goal -b
Number of occurances of word 'goal': 1
'''