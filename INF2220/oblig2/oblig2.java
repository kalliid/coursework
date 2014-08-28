import java.io.*;
import java.util.*;

class Project {
    /*
    A class for representing and doing critical path analysis of a 
    given project, consisting of tasks. The project is read in from
    an input file as an activity-node (node-weighted) graph, which
    is used internally by the class to build an event-node (edge-weighted)
    graph.
    */
    private int maxnr; // number of tasks in project
    private Task[] tasks;   // all tasks of the project
    private Event[] events; // events of the project, including dummies
    private ArrayList<Integer> topologicalOrder; 

    class Task {
        /*
        A task is a node in the activity-node graph. It is uniquely
        defined by its task id. It also contains the time and manpower
        the task takes to complete. And will after calculating it contain
        information about the earliest and latest start times of the task.
        A task also contains it's outward edges in a linked list
        */
        private int id, time, staff;
        private String name;
        private int earliestStart, latestStart, slack;
        private int earliestCompletion, latestCompletion;
        private LinkedList<TEdge> outEdges;
        private int cntPredecessors;
        private boolean active; // Used by DFS

        Task(int id) {
            this.id = id;
            outEdges = new LinkedList<TEdge>();
            cntPredecessors = 0;
            active = false;
        }

        private void addEdge(int id) {
            /*
            Adds an outward edge to the task, pointing to the task
            defined by the given id.
            */
            if (id == 0)
                return;
            cntPredecessors++;
            outEdges.add(new TEdge(id));    
        }
    }

    private class TEdge {
        /*
        A TEdge represents a directed edge in the activity-node graph. 
        The edge (u,v) means task u is dependant on task v.
        */
        private Task task;

        TEdge(int id) {
            task = getTask(id);
        }
    }

    private Task getTask(int id) {
        // Returns the task uniquely defined by a given id.
        return tasks[id-1];
    }

    Project (String inputfile) {
        /*
        Constructor for the project, reads an inputfile,
        creates all the tasks, and the edges between them
        */
        Scanner scanner = null;
        try {
            scanner = new Scanner(new File(inputfile));
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        } catch (NoSuchElementException e) {
            System.err.println("Error: " + e.getMessage());
        }

        // Read number of tasks and empty line
        maxnr = Integer.parseInt(scanner.nextLine());
        scanner.nextLine();

        // Generate alle the tasks
        tasks = new Task[maxnr];
        for (int id=1; id<=maxnr; id++)
            tasks[id-1] = new Task(id);

        // Read info on each task
        for (Task t : tasks) {
            // Read info on task t
            String line = scanner.nextLine();
            String[] taskInfo = line.split("\\s+");
            String name = taskInfo[1];
            int time = Integer.parseInt(taskInfo[2]);
            int staff = Integer.parseInt(taskInfo[3]);
            // Set info
            t.name = name;
            t.time = time;
            t.staff = staff;

            // Read the dependancies and create corresponding edges
            for (int j=4; j<taskInfo.length; j++) {      
                int dependancy = Integer.parseInt(taskInfo[j]);
                t.addEdge(dependancy);
            }
        }

        // Create an array to store a topological order of the project
        topologicalOrder = new ArrayList<Integer>();
    }

    private class Event {
        /*
        An event is a node in the event-node graph. It corresponds to
        either the completion of a task, or the completion of all of 
        an activitie's dependancies, or the project as a whole.
        The latter two cases we refer to as dummy events. The tasks are
        now edges between the events, and will be weighted by their time
        cost. Edges pointing to dummy events will have a cost of zero.
        Note that the id of an event does not uniquely identify it, as
        dummy and real events might have the same id.
        */
        int id;
        boolean dummy;
        LinkedList<EEdge> inEdges;
        LinkedList<EEdge> outEdges;
        int earliestCompletion, latestCompletion;

        Event(int id, boolean d) {
            this.id = id;
            inEdges = new LinkedList<EEdge>();
            outEdges = new LinkedList<EEdge>();
            dummy = d;
            earliestCompletion = 0;
            latestCompletion = Integer.MAX_VALUE;
        }

        private void addOutEdge(Event event, int time) {
            /*
            Adds an outward edge from this event to another event, this 
            automatically adds the edge as an inEdge for the target. Edges 
            are weighted by time (zero for edges pointing to dummy events.)
            */
            event.addInEdge(this, time);
            outEdges.add(new EEdge(event, time));
        }

        private void addInEdge(Event event, int time) {
             inEdges.add(new EEdge(event, time));
        }
    }

    private class EEdge {
        /*
        The edges between events. These edges corresponds to the tasks of
        the project, and so are weighted by time (zero for edges pointing to
        dummy events).
        */
        Event event;
        int time;

        EEdge(Event e, int t) {
            event = e;
            time = t;
        }
    }

    private Event getInEvent(int id) {
        // Returns the dummy event corresponding to the task of a given id.
        return events[2*id-2];
    }

    private Event getOutEvent(int id) {
        // Returns the real event corresponding to the task of a given id.
        return events[2*id-1];
    }

    private void constructEventEdgeGraph() {
        /*
        Constructs the event-node graph from the activity-node graph.
        For every task, we construct two events, called the in and out
        events, the inEvent is a dummy event. We also insert an edge from
        inEvent to the outEvent with a weight equal to the time of the task.
        For all the dependancy edges (u,v) in the activity-node graph, we 
        insert an event edge (v_out, u_in) with weight zero. We also construct
        a dummy event to represent the completion of the entire project.
        */
        events = new Event[2*maxnr+2];
        for (int id=1; id<=maxnr; id++) {
            events[2*id-2] = new Event(id, false); // inEvent
            events[2*id-1] = new Event(id, true);  // outEvent
            getInEvent(id).addOutEdge(getOutEvent(id), getTask(id).time);
        }
        for (Task t : tasks)
            for (TEdge e : t.outEdges)
                getOutEvent(e.task.id).addOutEdge(getInEvent(t.id), 0);

        // Add the dummy event representing the completion of the project
        events[2*maxnr] = new Event(0, false);
        events[2*maxnr+1] = new Event(0, false);
        getInEvent(maxnr+1).addOutEdge(getOutEvent(maxnr+1), 0);
        for (int i=0; i<2*maxnr; i++)
            events[i].addOutEdge(getInEvent(maxnr+1), 0);

        // The project event must be last in the topological order
        topologicalOrder.add(maxnr+1); 
    }

    private boolean dfs() {
        /*
        Performs a depth-first-search of the activity-node graph
        and constructs a (not necessarily the only) topological
        ordering of the tasks. If a backward edge is detected,
        the graph is cyclic and the project is not realizable.
        */
        HashMap<Task,Task> parent = new HashMap<Task,Task>();
        for (Task s : tasks) {
            if (!parent.containsKey(s)) {
                parent.put(s, null);
                parent = dfsVisit(parent, s);
                if (parent == null) {
                    // Current node is part of a cycle
                    System.out.println(" <- " + s.name);
                    return false;
                }
            }
        }
        return true;
    }

    private HashMap<Task,Task> dfsVisit (HashMap<Task,Task> parent, Task s) {
        /*
        Recursive depth-first search starting at a given node,
        if a cycle is detected, the recursion is broken and null
        is returned.
        */
        s.active = true;    // Mark current node as active
        // Loop over all edges
        for (TEdge e : s.outEdges) {
            Task t = e.task;
            if (t.active) {
                // An active node has been hit: a cycle is detected
                System.out.println("Project is not realizable, cycle:");
                System.out.print(t.name);
                return null;
            }
            if (!parent.containsKey(t)) {
                // Recursively visit new nodes
                parent.put(t, t);
                parent = dfsVisit(parent, t);
                if (parent == null) {
                    // Current node is part of a cycle
                    System.out.print(" <- " + t.name);
                    return null;
                }
            }
        }
        s.active = false;
        topologicalOrder.add(s.id);
        return parent;
    }

    private void findEarliestStartTimes() {
        /*
        Finds the earliest start times of all tasks by traversing
        the event-edge in topologicalOrder. We find the earliest
        completion time of all nodes from:
            EC1 = 0
            ECw = max(ECv + c(v,w)) for all event-edges (v,w)
        */
        for (Integer id : topologicalOrder) {
            Event[] events = {getInEvent(id), getOutEvent(id)};
            for (Event s : events)
                for (EEdge e : s.outEdges) {
                    int oldTime = e.event.earliestCompletion;
                    int newTime = s.earliestCompletion + e.time;
                    e.event.earliestCompletion = max(oldTime, newTime);
                }
        }
        for (Task t : tasks) {
            t.earliestCompletion = getOutEvent(t.id).earliestCompletion;
            t.earliestStart = t.earliestCompletion - t.time;
        }
    }

    private void findLatestStartTimes() {
        /*
        Computes the latest completion times of all events by 
        traversing the event-edge in reverse topological order,
        we find the latest completion time of all the nodes from:
            LCmaxnr = ECmaxnr
            LCv = min(LCw - c(v,w)) for all event-edges (v,w)
        */

        // For last event, latest and earliest times are equal
        Event lastEvent = getOutEvent(topologicalOrder.get(maxnr));
        lastEvent.latestCompletion = lastEvent.earliestCompletion;
        
        // Make a reverse iterator
        ListIterator<Integer> listIterator = 
                topologicalOrder.listIterator(topologicalOrder.size());

        while(listIterator.hasPrevious()){
            Integer id = listIterator.previous();
            Event[] events = {getOutEvent(id), getInEvent(id)};
            for (Event s : events)
                for (EEdge p : s.inEdges) {
                    int oldTime = p.event.latestCompletion;
                    int newTime = s.latestCompletion - p.time;
                    p.event.latestCompletion = min(oldTime, newTime);
                }
        }
        for (Task t : tasks) {
            t.latestCompletion = getOutEvent(t.id).latestCompletion;
            t.latestStart = t.latestCompletion - t.time;
        }
    }

    private void findSlack() {
        for (Task t : tasks)
            t.slack = t.latestStart - t.earliestStart;
    }

    private static int max(int n, int m) {
        return n > m ? n : m;
    }

    private static int min(int n, int m) {
        return n < m ? n : m;
    }

    public void criticalPathAnalysis() {
        /*
        Performs the critical path analysis of the project
        */
        // Asserts that the graph is acyclic and
        // finds a topological ordering of the tasks
        if (!dfs()) {
            System.out.println("Exiting program.\n");
            System.exit(0);
        }
        // Constructs the event edge graph
        constructEventEdgeGraph();
        // Finds earliest and latest start and completion time of all tasks
        findEarliestStartTimes();
        findLatestStartTimes();
        // Finds the slack of all tasks
        findSlack();
    }

    public void printTimes() {
        for (Task t : tasks) {
            System.out.println("Task id: " + t.id);
            System.out.println("\t Earliest completion: "
                                 + t.earliestCompletion);
            System.out.println("\t Latest completion: "
                                 + t.latestCompletion);
            System.out.println("\t Slack: " 
                                 + (t.latestCompletion-t.earliestCompletion));
        }
    }

    public void printCriticalTasks() {
        System.out.println("\n**** Critical Tasks ****");
        for (Task t : tasks)
            if (t.slack == 0)
                System.out.println("Task " + t.id + ", " + t.name);
    }

    public void printAllTasks() {
        System.out.println("**** Information on all tasks ****");
        for (Task t : tasks) {
            System.out.println("\nId: " + t.id);
            System.out.println("Name: " + t.name);
            System.out.println("Time: " + t.time);
            System.out.println("Staff: " + t.staff);
            System.out.println("Slack: " + t.slack);
            System.out.println("Latest starting time: " + t.latestStart);
            boolean flag = false;
            for (Task u : tasks) {
                for (TEdge v : u.outEdges)
                    if (v.task == t) {
                        if (!flag) {
                            flag = true;
                            System.out.println("The following tasks depend on this:");
                        }
                        System.out.println("\tTask " + u.id + ", " + u.name);                        
                    }
            }
            if (!flag)
                System.out.println("No tasks depend on this.");
        }
    }

    public void iterateThroughProject() {
        int time = -1;
        int finishedTasks = 0;
        int currentStaff = 0;
        boolean flag = false;
        System.out.println("\n**** Project work log ****");
        while (finishedTasks < maxnr) {
            time++;
            flag = false;
            for (Task t : tasks) {
                if (t.earliestStart == time) {
                    if (!flag) {
                        System.out.println("Time: " + time);
                        flag = true;
                    }
                    System.out.println("         Starting: " + t.id);
                    currentStaff = currentStaff + t.staff;
                }
                if (t.earliestCompletion == time) {
                    if (!flag) {
                        System.out.println("Time: " + time);
                        flag = true;
                    }
                    System.out.println("         Finished: " + t.id);
                    finishedTasks++;
                    currentStaff = currentStaff - t.staff;
                }
            }
            if (flag)
                System.out.println("    Current Staff: " + currentStaff);
        }
        System.out.format("\n**** Shortest possible project" + 
                          " execution is %d ****\n\n", time);
    }
}

class Oblig2 {
    public static void main(String[] args) {
        // Read command-line arguments
        if (args.length != 2) {
            String error="InputError, usage: java Oblig2 inputfile manpower";
            System.out.println(error);
            return;
        }
        
        String inputfile = args[0];
        int manpower = Integer.parseInt(args[1]);

        // Construct project from the given inputfile
        Project project = new Project(inputfile);

        // Perform critical path analysis of project
        project.criticalPathAnalysis();

        // Print results
        project.printAllTasks();
        project.printCriticalTasks();
        project.iterateThroughProject();
    }
}