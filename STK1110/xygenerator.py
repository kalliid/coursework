import sys

usage = '%s start:stop,step func' % sys.argv[0]

if len(sys.argv) != 3:
	print usage;sys.exit(1)

print sys.argv[1]