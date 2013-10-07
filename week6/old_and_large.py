import shutil
import sys
import os

# usage = '''Usage: %s directory
# Options:
#     -r      moves file to /tmp/trash''' % sys.argv[0]

# try:
#     directory = sys.argv[1]
#     remove = '-r' in sys.argv[2:]
# except :
#     print usage, sys.exit(1)
    
print os.path.isfile('findprograms.py')


def remove_file(filepath):
    # Make sure trash-folder exists
    if not os.path.isdir('/tmp/trash'):
        os.mkdir('/tmp/trash')
        print 'Made directory /tmp/trash'

    shutil.copy(filepath, '/tmp/trash')
    os.remove(filepath)



