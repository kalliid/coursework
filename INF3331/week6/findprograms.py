import os

def findprograms(programs, dirs=[]):
    '''
    Looks for the specified programs, and returns a dictionary 
    containing the programs' complete path on the current system.
    PATH is searched by default and additional directories can
    be specified using the dirs parameter.
    '''
    dictionary = {}

    for program in programs:
        # Check all paths in PATH and additional directories
        for path in os.environ["PATH"].split(os.pathsep) + dirs:
            # Create the filepath for the executable
            filepath = os.path.join(path, program)
            # Check if file exists and is executable
            if os.path.isfile(filepath) and os.access(filepath, os.X_OK):
                # Program exists on computer, move on to next program
                dictionary[program] = filepath
                break
            # Program does not exist, set value to None
            dictionary[program] = None       

    return dictionary



if __name__ == '__main__':
    # Example of use
    programs = {
        'gnuplot'  : 'plotting program',
        'gs'       : 'ghostscript, ps/pdf interpreter and previewer',
        'f2py'     : 'generator for Python interfaces to F77',
        'swig'     : 'generator for Python interfaces to C/C++',
        'convert'  : 'image conversion, part of the ImageMagick package',
        }

    installed = findprograms(programs.keys())
    
    for program in installed.keys():
        if installed[program]:
           print "You have %s (%s)" % (program, programs[program])
        else:
            print "*** Program %s was not found on the system" % (program,)


'''
user$ python findprograms.py 
You have convert (image conversion, part of the ImageMagick package)
You have gs (ghostscript, ps/pdf interpreter and previewer)
*** Program swig was not found on the system
You have gnuplot (plotting program)
You have f2py (generator for Python interfaces to F77)
'''