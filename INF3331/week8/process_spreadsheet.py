from numpy import array, sum

def process_spreadsheet(infile):
    # Read the inputfile
    with open(infile, 'r') as f: data = f.readlines()
    # Extract the names from the first column
    names = [l.split(',')[0] for l in data]  
    # Extract the numbers and sum them  
    nums = sum(array([l.split(',')[1:] for l in data], dtype='float'), axis=1)
    # Print the results
    print "\n".join([names[i]+" : "+str(nums[i]) for i in range(nums.size)])

if __name__ == '__main__':
    # Test the function on the example given in the exercise text
    process_spreadsheet('example.dat')

'''
user$ python process_spreadsheet.py
"activity 1" : 2719.0
"activity 2" : 128.0
"activity 3" : 365.5
'''









