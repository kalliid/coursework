from random import randint
import sys 

def ask(question):
    try: 
        answer = raw_input(question)
    # Abort on ctrl+d
    except EOFError:
        print ""; sys.exit() 
    return answer

def play_quiz():
    N = int(ask("How many questions do you want? "))
    level = int(ask("What difficulty level do you want?"
          + "\n\t1. Beginner"
          + "\n\t2. Intermediate"
          + "\n\t3. Advanced" 
          + "\nPick a number: "))
    question_type = int(ask("What type of questions do you want?" 
            + "\n\t1. Addition"
            + "\n\t2. Subtraction"
            + "\n\t3. Multiplication"
            + "\n\t4. Mixed"
            + "\nPick a number: "))

    C = 0
    maxoperand = [1, 10, 25, 100][level]

    def add(x, y):
        return x + y, '+'
    def sub(x, y):
        return x - y, '-'
    def prod(x, y):
        return x * y, '*'
    def mix(x, y):
        return [add, sub, prod][randint(0,2)](x, y)
    
    operator = [0, add, sub, prod, mix][question_type]

    for i in range(N):
        n1 = randint(1, maxoperand)
        n2 = randint(1, maxoperand)

        result, op = operator(n1, n2)
        ans = int(ask("\nWhat's %d %s %d?\nAnswer: " % (n1, op, n2)))
        if ans == result:
            print "That's right -- well done."
            C = C + 1
        else:
            print "No, I'm afraid the answer is %d.\n" % result

    print "\n" + "*"*26 \
         +"\nI asked you %d questions. You got %d of them right." % (N, C)

    if C/float(N) > 2./3:
        print "Well done!"
    elif C/float(N) > 1./3:
        print "You need more practice"
    else:
        print "Please ask your math teacher for help!"

if __name__ == "__main__":
    play = "y"
    while play == "y":
        play_quiz()
        y = ask("\nWould you like to play again? (y/n)\nAnswer: ")