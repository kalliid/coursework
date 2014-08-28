numbers = [15,78,56,25,19,38,57,76,34,53,72,91]

hashTable = {}

def f(i, x):
    R = 17
    return i*(R - (x % R))

for x in numbers:
    for i in range(1000):
        key = (x + f(i,x)) % 19
        if key not in hashTable:
            hashTable[key] = x
            break

print hashTable