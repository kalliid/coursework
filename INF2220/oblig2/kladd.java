import java.io.*;
import java.util.*;

class Project {
    /*
    Class for representing a project and doing a critical path
    analysis on the project. The project consists of a number of
    given tasks. The project is read in from an inputfile as a
    activity-node graph, and is then converted to an event-node
    graph.
    */
    private int maxnr;      // number of tasks in project
    private Task[] tasks;   // all tasks of the project
    private Event[] events; // events of the project
    private ArrayList<Integer> topologicalOrder;

    private class Edge {
        /*
        Class for representing the dependancies as edges,
        these are stored as linked lists in the Task-objects.
        */
        private Task task;
        private Edge next;

        Edge(int id) {
            task = getTask(id);
            next = null;
        }
    }

    private class Task {
        /*
        Class for representing the tasks of the project
        and their properties. Their dependancies are stored
        as a linked-list of Edge-objects.
        */
        private int id, time, staff;
        private String name;
        private int earliestStart, latestStart;
        private Edge outEdges;
        private int cntPredecessors;
        private boolean active;
        private int earliestCompletion, latestCompletion, slack;

        Task(int id) {
            this.id = id;
            outEdges = null;
            cntPredecessors = 0;
            active = false;
        }

        private void addEdge(int id) {
            // Adds a dependancy edge pointing to a task with given id
            if (id == 0)
                return;
            cntPredecessors++;
            if (outEdges == null) {
                outEdges = new Edge(id);
                return;
            }
            Edge e = outEdges;
            while (e.next != null)
                e = e.next;
            e.next = new Edge(id);
        }
    }

    private class Event {
        /* 
        Class for representing an event, which corresponds to the
        completion of an activity, or the completition of 
        all of an activity's dependancies, or the project as a whole.
        The latter two cases we refer to as dummy events.
        */
        int id;
        boolean active;
        boolean dummy;
        EventEdge outEdges;
        EventEdge predecessors;
        int earliestCompletion;
        int latestCompletion;

        Event(int id, boolean d) {
            this.id = id;
            outEdges = null;
            active = false;
            dummy = d;
            earliestCompletion = 0;
            latestCompletion = 999;
        }

        void addEdge(Event event, int time) {
            /*
            Method for adding an outward edge from this event to
            another event. EventEdges are stored as a linked list. 
            */
            event.addPredecessor(this, time);

            if (outEdges == null) {
                outEdges = new EventEdge(event, time);
                return;
            }

            EventEdge e = outEdges;
            while (e.next != null)
                e = e.next;
            e.next = new EventEdge(event, time);
        }

        void addPredecessor(Event event, int time) {
            /*
            Method for adding a predecessor from this event to 
            another event. Predecessors are stored as a linked list.
            */
            if (predecessors == null) {
                predecessors = new EventEdge(event, time);
                return;
            }

            EventEdge e = predecessors;
            while (e.next != null)
                e = e.next;
            e.next = new EventEdge(event, time);
        }
    }

    private class EventEdge {
        /*
        Class for representing the edges between events.
        These edges correspond to the task of the project,
        and so they have a time-weight. EventEdges that 
        point to a dummy event will have a weight of zero.
        */
        int time;
        Event event;
        EventEdge next;

        EventEdge(Event e, int t) {
            this.time = t;
            this.event = e;
            next = null;
        }
    }

    Project (String inputfile) {
        /*
        Constructor for the project, reads an inputfile,
        creates all the tasks, and the edges between them
        */
        // Create scanner-object
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

        // Generate the tasks
        tasks = new Task[maxnr];
        for (int i=0; i<maxnr; i++)
            tasks[i] = new Task(i+1);

        // Read info on each task
        for (int i=0; i<maxnr; i++) {
            String line = scanner.nextLine();
            String[] taskInfo = line.split("\\s+");
            
            String name = taskInfo[1];
            int time = Integer.parseInt(taskInfo[2]);
            int staff = Integer.parseInt(taskInfo[3]);

            tasks[i].name = name;
            tasks[i].time = time;
            tasks[i].staff = staff;

            // Read the dependancies and create corresponding edges
            for (int j=4; j<taskInfo.length; j++) {      
                int dependancy = Integer.parseInt(taskInfo[j]);
                tasks[i].addEdge(dependancy);
            }
        }

        // Create an array to store a topological order of the project
        topologicalOrder = new ArrayList<Integer>();
    }

    private Task getTask(int id) {
        /*
        Returns the Task-object of a given id from the graph
        */
        return tasks[id-1];
    }

    public boolean checkRealizable() {
        /*
        Checks if the given project is realizable. The entire
        activity-node graph is visited using a depth-first-search.
        If an active node is hit, we have found a backward edge,
        i.e., the graph is cyclic and not realizable.
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
        for (Edge e=s.outEdges; e!=null; e=e.next) {
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

    public void convertGraph () {
        /*
        Constructs the event-node graph from the activity-node graph. We 
        construct dummy events.
        */
        events = new Event[2*maxnr+2];
        for (int id=1; id<=maxnr; id++) {
            // Create two event nodes for every task
            events[2*id-2] = new Event(id, false);
            events[2*id-1] = new Event(id, true);
            // Connect the events by an edge of weight task.time
            getInEvent(id).addEdge(getOutEvent(id),getTask(id).time);
        }
        for (Task t : tasks)
            // For all edges in the task-graph, add EventEdges of zero weight
            for (Edge e=t.outEdges; e!=null; e=e.next)
                getOutEvent(e.task.id).addEdge(getInEvent(t.id), 0);

        // Add a dummy event for the completetion of the whole project,
        // i.e. the completetion of all tasks.
        events[2*maxnr] = new Event(0, false);
        events[2*maxnr+1] = new Event(0, false);
        getInEvent(maxnr+1).addEdge(getOutEvent(maxnr+1), 0);
        for (int i=0; i<2*maxnr; i++)
            events[i].addEdge(getInEvent(maxnr+1), 0);

        topologicalOrder.add(maxnr+1);
    }

    private Event getInEvent(int id) {
        return events[2*id-2];
    }

    private Event getOutEvent(int id) {
        return events[2*id-1];
    }

    public ArrayList<Event> topologicalSort() {
        /*
        Finds a topological order (not neccesairly the only one)
        of the event-node graph, using a DFS.
        */
        ArrayList<Event> topological = new ArrayList<Event>();
        HashMap<Event,Event> parent = new HashMap<Event,Event>();
        for (Event s : events) {
            if (!parent.containsKey(s)) {
                parent.put(s, null);
                parent = dfsVisit(parent, s, topological);
            }
        }
        return topological;
    }

    private HashMap<Event,Event> dfsVisit (HashMap<Event,Event> parent, Event s, ArrayList<Event> topological) {
        /*
        Recursive depth-first search starting at a given node.
        */
        s.active = true;    // Mark current node as active
        // Loop over all edges
        for (EventEdge e=s.outEdges; e!=null; e=e.next) {
            Event t = e.event;
            if (!parent.containsKey(t)) {
                // Recursively visit new nodes
                parent.put(t, t);
                parent = dfsVisit(parent, t, topological);
            }
        }
        s.active = false;
        topological.add(s);
        return parent;
    }

    public void findEarliestCompletionTimes() {
        /*
        Computes the earliest completion times of all events by 
        traversing the event-edge in topological order, we find 
        the earliest completetion time of all the nodes from:
            EC1 = 0
            ECw = max(ECv + c(v,w)) for all event-edges (v,w)
        */
        for (Integer id : topologicalOrder) {
            Event[] events = {getInEvent(id), getOutEvent(id)};
            for (Event s : events)
                for (EventEdge e = s.outEdges; e!=null; e=e.next) {
                    int oldTime = e.event.earliestCompletion;
                    int newTime = s.earliestCompletion + e.time;
                    e.event.earliestCompletion = max(oldTime, newTime);
            }
        }
        for (Task t : tasks) {
            t.earliestCompletion = getOutEvent(t.id).earliestCompletion;
        }
    }

    public void findLatestCompletionTimes() {
        /*
        Computes the latest completion times of all events by
        traversing the event-edge in reverse topological order,
        we find the latest completion time of all the nodes from:
            LCmaxnr = ECmaxnr
            LCv = min(LCw - c(v,w)) for all event-edges (v,w)
        */

        // Make a deep copy of topologicalOrder and reverse it;
        ArrayList<Integer> reverseTopologicalOrder = new ArrayList<Integer>();
        for (Integer id : topologicalOrder) reverseTopologicalOrder.add(id);
        Collections.reverse(reverseTopologicalOrder);

        // For last event, latest and earliest times are equal
        Event lastEvent = getOutEvent(reverseTopologicalOrder.get(0));
        lastEvent.latestCompletion = lastEvent.earliestCompletion;
        
        for (Integer id : reverseTopologicalOrder) {
            Event[] events = {getOutEvent(id), getInEvent(id)};
            for (Event s : events)
                for (EventEdge p = s.predecessors; p!=null; p=p.next) {
                    int oldTime = p.event.latestCompletion;
                    int newTime = s.latestCompletion - p.time;
                    p.event.latestCompletion = min(oldTime, newTime);
                }
        }
        for (Task t : tasks) {
            t.latestCompletion = getOutEvent(t.id).latestCompletion;
        }
    }

    private static int max(int n, int m) {
        return n > m ? n : m;
    }

    private static int min(int n, int m) {
        return n < m ? n : m;
    }

    public void printTimes() {
        for (Task t : tasks) {
            System.out.println("Task id: " + t.id);
            System.out.println("\t Earliest completion: " + t.earliestCompletion);
            System.out.println("\t Latest completion: " + t.latestCompletion);
            System.out.println("\t Slack: " + (t.latestCompletion - t.earliestCompletion));
        }
    }

    public void printEarliestCompletionTimes() {
        for (Task t : tasks) {
            System.out.println(t.id + " " + getOutEvent(t.id).earliestCompletion);
        }
    }

    public void printLatestCompletionTimes() {
        for (Task t : tasks) {
            System.out.println(t.id + " " + getOutEvent(t.id).latestCompletion);
        }
    }

    public void printLatestStartingTimes() {
        for (Task t : tasks) {
            System.out.println(t.id + " " + getInEvent(t.id).latestCompletion);
        }
    }

    public void findSlack() {
        for (Task t : tasks) {
            int earliest = getOutEvent(t.id).earliestCompletion;
            int latest = getOutEvent(t.id).latestCompletion;
            int slack = latest-earliest;
            t.slack = slack;
        }
    }

    public void printSlack() {
        for (Task t : tasks) {
            int earliest = getOutEvent(t.id).earliestCompletion;
            int latest = getOutEvent(t.id).latestCompletion;
            int slack = latest-earliest;
            System.out.println(t.id + " " + slack);
        }
    }

    public void printCriticalTasks() {
        System.out.println("Critical Tasks:");
        for (Task t : tasks)
            if (t.slack == 0)
                System.out.println(t.id);
    }

        //     Event outEvent = getOutEvent(id);

        //     System.out.println(getInEvent(id));
        // }
        // // for (int i=0; i<2*maxnr;i++)
        // //     System.out.println(topological.get(i).id);
        // // for (Event t : topological) {
        // //     System.out.println("FIRST: " + t.id + t.outEdges);
        // //     for (EventEdge e = t.outEdges; e!=null; e=e.next) {
        // //         int oldTime = e.event.earliestCompletion;
        // //         int newTime = t.earliestCompletion + e.time;
        // //         e.event.earliestCompletion = max(oldTime, newTime);
        // //         System.out.println(e.event.id + " " + max(oldTime,newTime));
        // //     }
        // // }
        // // for (Task t : tasks) {
        // //     System.out.println(t.id + " " + getOutEvent(t.id).earliestCompletion);
        // // }


    public void printAllEvents() {
        System.out.println(getInEvent(5).dummy);
        for (Event s : events) {
            System.out.print("\n"+s.id + " (" + s.dummy + ") points to\n\t");
            for (EventEdge e = s.outEdges; e!=null; e=e.next) {
                System.out.print(e.event.id + "(" + e.event.dummy + ")");
            }
        }
    }

    public void printTopologicalOrder() {
        for (Integer i : topologicalOrder)
            System.out.println(i);
    }

    private Event findStartingEvent() {
        for (Task t : tasks) {
            if (t.cntPredecessors == 0) {
                return getInEvent(t.id);
            }
        }
        return null;
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

        // Check if project is realizable
        if (!project.checkRealizable()) {
            System.out.println("Exiting program.");
            return;
        }

        // Convert activity-node graph to event-node graph
        project.convertGraph();


        project.printTopologicalOrder();
        // project.printTopologicalOrder();
        // project.printAllEvents();
        project.findEarliestCompletionTimes();
        project.findLatestCompletionTimes();
        //project.printEarliestCompletionTimes();
        //project.printLatestStartingTimes();
        //project.printSlack();
        //project.printTimes();
        project.findSlack();
        project.printCriticalTasks();

        System.out.println(Integer.MAX_VALUE);
    }
}