def gettime(lines):
    """Reads a text made by jhead and extracts the date and time"""
    date, time = [l.split()[2:] for l in lines if l[:9]=="Date/Time"][0]
    return tuple(date.split(':')), tuple(time.split(':'))

def prefix(date, time, string):
    """Adds date and time to a string as prefix, if the input string
    already contains the date and time, it is returned unchanged."""
    if len(string.split("__")) == 3: return string
    return "__".join(("_".join(date), "_".join(time), string))


if __name__ == '__main__':
    # Read in sample text from file
    infile = open('jhead.sample.txt', 'r')
    lines = infile.readlines()
    infile.close()

    # Extract date and time from sample text 
    date, time = gettime(lines)

    # Add date and time to example filename
    name = "img_4978.jpg"
    altered_name = prefix(date, time, name)
    print altered_name

    # Try to add date and time again
    print prefix(date, time, altered_name)

'''
user$ python jpegrename.py 
2002_05_19__18_10_03__img_4978.jpg
2002_05_19__18_10_03__img_4978.jpg
'''