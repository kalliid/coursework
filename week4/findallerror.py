import re

real = r"\s*(?P<number>-?(\d+(\.\d*)?|\d*\.\d+)([eE][+\-]?\d+)?)\s*"
pattern = re.compile(real)

some_interval = "[3.58e+05132 , 6E+09]"

# Create an iterator over MatchObject instances
matches = pattern.finditer(some_interval)

# Loop over iterator and extract 'number'-groups
boundaries = [m.group('number') for m in matches]

# Print out resulting boundaries
print '\n'.join(boundaries)

'''
user$ python findallerror.py 
3.58e+05132
6E+09
'''