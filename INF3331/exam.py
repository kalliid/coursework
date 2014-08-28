integer = r'\d+'
decimal = r'\d+\.\d*|\d*\.\d+'
scientific = r'(%s|%s)[Ee][+\-]?\d+' % (decimal, integer)

real = r'-?(%s|%s|%s)' % (scientific, decimal, integer)

pattern = r'\[\s*(?P<lower>%s)\s*,\s*(?P<upper>%s)\s*\]' % (real, real)

import re

print "real"
hits = re.finditer(real, '[ -3.14E+00, 29.6524]')
print "\n".join([hit.group()for hit in hits])

print "\n\n\npattern\n"
hits = re.finditer(pattern, '[ -3.14E+00, 29.6524]')
print "\n".join(["%s\t%s" % hit.group('lower', 'upper') for hit in hits])

