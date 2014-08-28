I have chosen not to implement the optional part of the assignment.

The normal tasks are solved as outlined on pages 401 and 402 of Weiss. Meaning two tasks are built, the "normal" activity-node graph given by the output file
but also a event-node graph. For ease of implementation, more dummy nodes than
needed are constructed, and so the complexitity will be worse than optimal.

The complexity for the task of checking realizable is O(E+V), as it is a depth
-first-search. The complexity for building the event-node graph is also 
O(E+V), as there are a constant number of operations per node and per edge in
the activity-node graph. Traversing the event-node graph will also be O(E+V) as each node and edge is visited once, although with worse constants than optimal. The complexity of the entire program is thusly O(E+V).

The program should run fine with the commands listed in the assignment text. The file output.txt has been made by running the following commands in a terminal:

user$ javac oblig2.java
user$ echo "user$ java Oblig2 buildhouse1.txt 999" >> output.txt
user$ java Oblig2 buildhouse1.txt 999 >> output.txt
user$ echo "user$ java Oblig2 buildhouse2.txt 999" >> output.txt
user$ java Oblig2 buildhouse2.txt 999 >> output.txt
user$ echo "user$ java Oblig2 buildrail.txt 999" >> output.txt
user$ java Oblig2 buildrail.txt 999 >> output.txt
