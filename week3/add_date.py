def add_date(string):
	"""Appends current system date to a given string"""
	from time import ctime

	# Get current system date
	now = ctime()
	month = now[4:7]
	mday  = now[8:10]
	year  = now[20:24]
	append = "_%s%s_%s" % (month, mday, year)

	return string+append

if __name__ == '__main__':
	print add_date('myfile')

'''
user$ python add_date.py
myfile_Sep11_2013
'''
