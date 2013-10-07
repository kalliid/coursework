def join(delimiter, *args):
    """Function for joining strings, and tuples/lists of strings"""
    string = args[0] if type(args[0])== str else delimiter.join(args[0])
    for arg in args[1:]:
        if type(arg) == str:
            string += delimiter + arg
        else:
            string += delimiter + delimiter.join(arg)

    return string

if __name__ == "__main__":
    # Example of use
    list1 = ['s1','s2','s3']
    tuple1 = ('s4', 's5')
    ex1 = join(' ', 't1', 't2', list1, tuple1, 't3', 't4')
    ex2 = join('  #  ', list1, 't0')
    print ex1
    print ex2

'''
user$ python join.py 
t1 t2 s1 s2 s3 s4 s5 t3 t4
s1  #  s2  #  s3  #  t0
'''
