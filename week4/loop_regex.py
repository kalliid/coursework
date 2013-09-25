loop1 = '[0:12]'     # 0,1,2,3,4,5,6,7,8,9,10,11,12
loop2 = '[0:12, 4]'  # 0,4,8,12
r = r'\[\s*(\d+)\s*:\s*(\d+)\s*,?\s*(\d*)\]'
r = r'\[\s*(\d+)\s*:\s*(\d+)\s*,?\s*(\d*)\s*\]'
import re
print re.search(r, loop1).groups()
print re.search(r, loop2).groups()

'''
user$ python loop_regex.py 
('0', '12', '')
('0', '12', '4')
'''



