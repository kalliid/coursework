import shutil
import time
import sys
import os

def remove_file(filepath):
    '''Moves a given file into tmp/trash'''
    # Make sure trash-folder exists
    if not os.path.isdir('/tmp/trash'):
        os.mkdir('/tmp/trash')
        print 'Made directory /tmp/trash'

    # Copy file into trash-folder, then remove original
    shutil.copy(filepath, '/tmp/trash')
    os.remove(filepath)

def check_tree(tree, sizetol, agetol, remove=False):
    '''
    Walk over all files in a given tree and
    check age and size against tolerances, print out
    all violations and remove if wanted.
    '''
    violations = []
    # Iteratve over tree recursively
    for directory in os.walk(tree):
        dirpath, dirnames, filenames = directory
        for name in filenames:
            # Find full path of file
            path = os.path.join(dirpath, name)
            # Find size in MB
            size = os.path.getsize(path)/(1024.**2)
            # Find time since last access in days
            age = (time.time() - os.path.getatime(path))/86400.  
            if age > agetol and size > sizetol:
                # Store violation
                violations.append((path, size, age))
                # Remove file if wanted
                if remove:
                    remove_file(path)

    return violations
 
def _test():
    '''Function for testing the program using fakefiletree.py'''
    # Create a tree with files of random age and size for testing
    if os.path.isdir('tmptree'): shutil.rmtree('tmptree')
    print "Generating fake tmptree data"
    os.system("python fakefiletree.py tmptree")
    print "Done generating data \n\n\nTesting:"

    # Find number of all files in tmptree
    n = len(check_tree('tmptree', 0, 0, remove=False))
    
    # Find and remove violations in tmptree
    violations = check_tree('tmptree', 2, 100, remove=True)
    print "The following violations have been removed:"
    for v in violations:
        print 'File:  %s\nSize:  %.2f MB\nAge:   %d days' % (v[0], v[1], v[2])

    print "%d of %d files have been removed" % (len(violations), n)

    # List files in /tmp/trash
    print "The files in /tmp/trash are now"
    for f in os.listdir('/tmp/trash'):
        print f

    # Remove tmptree from system and clean /tmp/trash
    shutil.rmtree("tmptree")
    shutil.rmtree("/tmp/trash")
    os.mkdir('/tmp/trash')

    print "\nTesting finished without error."
    sys.exit(0)


if __name__ == "__main__":
    usage = '''Usage: %s
    Input:
        tree    tree to be checked for files recursively
        sizetol tolerance of filesize in MB
        agetol  tolerance of file age in days
    Options:
        -r      moves file to /tmp/trash
        -t      test using fakefiltree.py''' % sys.argv[0]

    # Catches testing flag
    if '-t' in sys.argv:
        _test()

    # Read cmd-line arguments
    try:
        tree = sys.argv[1]
        sizetol = float(sys.argv[2])
        agetol = float(sys.argv[3])
        remove = '-r' in sys.argv
    except:
        print usage, sys.exit(1)

    # Find violations
    violations = check_tree(tree, sizetol, agetol, remove=remove)

    # Print findings
    p = 'The following violations' if violations else 'No violations'
    r = ' and removed' if remove else ''
    print "%s have been found in %s%s:" % (p, tree, r)
    for v in violations:
        print 'File:  %s\nSize:  %.2f MB\nAge:   %d days' % (v[0], v[1], v[2])            


'''
user$ python old_and_large.py -t
Generating fake tmptree data
[...]
generated 7 files and 3 directories
Done generating data 

Testing:
The following violations have been removed:
File:  tmptree/tmpf-165459
Size:  9.38 MB
Age:   223 days
File:  tmptree/tmpf-544825
Size:  9.33 MB
Age:   237 days
File:  tmptree/tmpf-19120
Size:  5.39 MB
Age:   166 days
File:  tmptree/tmpf-391976/tmpf-93296
Size:  8.49 MB
Age:   214 days
File:  tmptree/tmpf-160372/tmpf-188037
Size:  2.16 MB
Age:   168 days
5 of 7 files have been removed
The files in /tmp/trash are now
tmpf-93296
tmpf-165459
tmpf-544825
tmpf-19120
tmpf-188037

Testing finished without error.
'''