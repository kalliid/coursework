from numpy import array, sum

data = open('example.dat', 'r').readlines()
names = [l.split(',')[0] for l in data]
numbers = sum(array([l.split(',')[1:] for l in data], dtype='float'),axis=1)
print "\n".join(['%s : %s' % (name, num) for name, num in zip(names,numbers)])


'''
user$ python process_spreadsheet.py








