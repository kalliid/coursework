import java.io.*;
import java.util.*;

class TaskGraph {
    /*
    Class for representing a set of tasks as a directed graph,
    and estimating an optimal working-plan
    */

    private int n;  // Number of nodes
    private Task[] tasks;

    TaskGraph(String inputfile) {
        /*
        Generate a TaskGraph for a given project using inputfile
        */
        Scanner inputscanner = create_scanner(inputfile);
        generateGraph(inputscanner);
    }

    private Scanner create_scanner(String filename) {
        /*
        Create Scanner object for reading inputfile
        */
        Scanner scanner = null;
        try {
            scanner = new Scanner(new File(filename));
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        } catch (NoSuchElementException e) {
            System.err.println("Error: " + e.getMessage());
        }
        return scanner;
    }

    private void generateGraph(Scanner scanner) {
        /*
        Uses the scanner object to generate the TaskGraph
        */
        // Read number of tasks, and skip blank line
        n = Integer.parseInt(scanner.nextLine());
        scanner.nextLine();
        
        // Add tasks
        for (int i=0; i<n; i++) {
            String line = scanner.nextLine();
            String[] task_info = line.split("\\s+");
            add_task(task_info);
            tasks[i] = task;
        }
    }

    private Task add_task(String[] task_info) {
        /*
        Adds a task into the graph and set up dependancies
        */
        int id = Integer.parseInt(task_info[0]);
        String name = task_info[1];

        Task new_task = new Task(id, name);
 
        for (int i=2; i<task_info.length; i++) {
            int d = Integer.parseInt(task_info[i]);
            new_task.add_dependancy(d);
        }

        return new_task;
    }

    private class Task {
        /*
        Class for representing a single task, i.e., a node
        */
        int id;
        String name;
        Element first;

        private class Element {
            int value;
            Element next;

            Element(int v) {
                value = v;
                next = null;
            }
        }

        Task(int id, String name) {
            this.id = id;
            this.name = name;
            first = null;
        }

        private void add_dependancy(int d) {
            Element e = first;
            if (first == null) {
                first = new Element(d);
                return;    
            }

            while (e.next != null)
                e = e.next;
            e.next = new Element(d);
        }
    }
}

class ExampleProject {
    public static void main(String[] args) {
        String inputfile = "buildhouse1.txt";
        TaskGraph project = new TaskGraph(inputfile);
    }
}

/*
class FileReader {
    
    Class for reading words from a given file into
    a BinarySearchTree.
    
    private Scanner scanner;

    FileReader(String filename) {
        // Create Scanner object
        try {
            scanner = new Scanner(new File(filename));
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        } catch (NoSuchElementException e) {
            System.err.println("Error: " + e.getMessage());
        }
        int k = 0;
    }
    
    public void readIntoTree(BinarySearchTree tree) {
        // Reads all words in the file and inserts them into a given BST
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            String[] words = line.split(" ");
            for (int i=0; i<words.length; i++)
                tree.insert(words[i]);
        }
        scanner.close();
    }
}
*/