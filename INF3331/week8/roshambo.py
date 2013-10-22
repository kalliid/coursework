from random import randint
import sys

def ask(question):
    print question,
    answer = sys.stdin.readline()
    # Abort on ctrl+d
    if answer == '' : sys.exit()
    print ""
    return answer

def win():
    print "Human: %7s\tComputer: %7s\tHuman wins!" % (n[human], n[comp])
    wins[0] += 1
    print "Score: Human %d \t Computer %d\n" % (wins[0], wins[1])

def draw():
    print "Human: %7s\tComputer: %7s\tA draw" % (n[human], n[comp])
    print "Score: Human %d \t Computer %d\n" % (wins[0], wins[1])

def loss():
    print "Human: %7s\tComputer: %7s\tComputer wins!" % (n[human], n[comp])
    wins[1] += 1
    print "Score: Human %d \t Computer %d\n" % (wins[0], wins[1])

p = {'r\n':0, 's\n':1, 'p\n':2}
n = {0:'rock', 1:'scissors', 2:'paper'}
results = {-2:loss, -1:win, 0:draw, 1:loss, 2:win}
wins = [0, 0]

print "Welcome to rock, paper, scissors!\n"
while True:
    try:
        required_to_win = int(ask("How many points are required to win? "))
        break
    except ValueError:
        print "Sorry, I did not understand that number. Please try again."
while required_to_win not in wins:
    while True:
        try:
            human = p[ask("Choose (r)ock, (p)aper, or (s)cissors? ")]
            break
        except KeyError:
            print "Sorry, the only legal moves are r, p or s."
    comp = randint(0, 2)
    results[human-comp]()
print "Final Score: Human %d \t Computer %d" % (wins[0], wins[1])

'''
user$ python roshambo.py
Welcome to rock, paper, scissors!

How many points are required to win? 2
 
Choose (r)ock, (p)aper, or (s)cissors? r
 
Human:    rock  Computer:   paper   Computer wins!
Score: Human 0   Computer 1

Choose (r)ock, (p)aper, or (s)cissors? p
 
Human:   paper  Computer:   paper   A draw
Score: Human 0   Computer 1

Choose (r)ock, (p)aper, or (s)cissors? r
 
Human:    rock  Computer:   paper   Computer wins!
Score: Human 0   Computer 2

Final Score: Human 0     Computer 2
'''