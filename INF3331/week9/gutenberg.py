def read_words(infile):
    # Read text from file
    with open(infile, 'r') as f:
        # Skip header of file
        l = ""; lines = []
        while "START OF THIS PROJECT GUTENBERG EBOOK" not in l:
            l = f.readline()
        # Read untill the end of the book
        while True:
            lines.append(f.readline())
            if "END OF THIS PROJECT" in lines[-1]:
                break

    words = {}
    # Read in words
    for l in lines:
        for w in l.split():
            word = filter(str.isalpha, w.strip())
            if word:
                if word not in words.keys():
                    words[word] = 1
                else:
                    words[word] += 1

    return words

def print_by_occurance(words):
    words = [[words[k], k] for k in words.keys()]
    words.sort(key=lambda word: word[0])
    words.reverse()
    for word in words:
        print "%25s %5d" % (word[1], word[0])

def print_alphabetically(words):
    keys = [k for k in words.keys()]
    keys.sort()
    for key in keys:
        print "%25s %5d" % (key, words[key])

if __name__ == "__main__":
    print "Alice in Wonderland, words in decreasing number of occurances:"
    infile = "AliceInWonderland.txt"
    words = read_words(infile)
    print_by_occurance(words)
    print "The Prince, words in alphabetical order:"
    infile = "ThePrince.txt"
    words = read_words(infile)
    print_alphabetically(words)

'''
user$ python gutenberg.py
Alice in Wonderland, words in decreasing number of occurances:
                      the  1515
                      and   774
                       to   717
                        a   610
                      ...   ...
                aftertime     1
                    knelt     1
                    saves     1
                      Tut     1
The Prince, words in alphabetical order:
                        A    23
                  ABILITY     1
                 ACQUIRED     3
                      ...   ...
                    youth     8
                     zeal     1
                   zenith     1
'''