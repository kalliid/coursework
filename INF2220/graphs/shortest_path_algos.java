import java.util.*

class Graph {
    private Vertex[] vertices;

    private class Vertex {
        int inorder;
        int topNum;
        Vertex[] adj;
        int dist;
        boolean visited;
    }

    void topologicalSort() throws CycleFoundException {
        /*
        A topological sort is an ordering of vertices in a directed acyclic graph, such that if there is a path from v_i to v_j, ten v_j appears after v_i in the ordering."

        Algo: We maintain a field of the inorder degree of all vertices. Any Vertex with inorder 0 is removed from the graph, along with its edges

        Complexity: O(|E|+|V|)
        */

        // Create a queue of vertices
        LinkedList<Vertex> q = new LinkedList<Vertex>(); 
        int counter = 0;

        // Go through all vertices in graph
        for (Vertex v : vertices)
            if (v.indegree == 0)
                // enqueue v
                q.add(v) 

        while (!q.isEmpty()) {
            Vertex v = q.remove(); // dequeue v
            v.topNum = ++counter;

            // Go through all adjacent vertices to v
            for (Vertex w : v.adj)
                if (--w.indegree == 0)
                    q.add(w);
        }

        if (counter != vertices.length)
            throw new CycleFoundException();
    }

    void breadth_first_search(Vertex s) {
        /*
        Start at a given Vertex s, visit all vertices at depth 1, then all vertices at depth 2, etc. The depth then also corresponds to the unweighted shortest path from s to any given Vertex.
        */

        for (Vertex v : vertices) {
            v.dist = INF;
        }

        LinkedList<Vertex> q = new LinkedList<Vertex>();
        s.dist = 0;
        q.add(s)

        while (!q.isEmpty()) {
            Vertex v = q.remove();

            for (Vertex w : v.adj)
                if (w.dist == INF) {
                    w.dist = w.dist + 1;
                    w.path = v;
                    q.add(w);
                }
        }
 
        for (int currDist =0; currDist < vertices.length; currDist++)
            for (Vertex v : vertices)
                if (!v.known && v.dist == currDist) {
                    v.known = true;
                    for (Vertex w : v.adj)
                        if (w.dist == INFINITY) {
                            v.dist = currDist + 1;
                            w.path = v;
                        }
                }

    }

    void dijkstra(Vertex s) {
        /*
        A single-source shortest path solver for any DG with no negative costs.
        */

        for (Vertex v : vertices) {
            v.dist = INF;
            v.known = false;
        }

        s.dist = 0;

        while (there is unknown distance vertex) {
            Vertex v = smallest unknown distance vertex;

            v.known = true;

            for (Vertex w : v.adj)
                if (!w.known) {
                    DistType cvw = cost of edge from v to w;

                    if (v.dist + cvw < w.dist) {
                        decrease(w.dist to v.dist + cvw);
                        w.path = v;
                    }
                }
        }
    }

    void acyclic_dijkstra(Vertex s) {
        // Create a queue of vertices
        LinkedList<Vertex> q = new LinkedList<Vertex>(); 
        int counter = 0;

        // Go through all vertices in graph
        for (Vertex v : vertices) {
            v.dist = INF;
            v.known = false;
            if (v.indegree == 0)
                // enqueue v
                q.add(v) 
        }

        s.dist = 0;

        while (!q.isEmpty()) {
            Vertex v = q.remove(); // dequeue v
            v.topNum = ++counter;

            DistType cvw = cost of edge from v to w;

                    if (v.dist + cvw < w.dist) {
                        decrease(w.dist to v.dist + cvw);
                        w.path = v;
                    }

            // Go through all adjacent vertices to v
            for (Vertex w : v.adj)
                if (--w.indegree == 0)
                    q.add(w);
        }

        if (counter != vertices.length)
            throw new CycleFoundException();
    }
    
    /*
    a[][] contains adj matrix, a[i][i] = 0
    d[] contains the values of the shortest path.
    vertices are numbered starting at 0; all arrays have
    equal dimension. A negative cycle exists if
    d[i][i] is set to a negative value. Actual pa
    */
    public static void allPairs(int[][] a, int[][] d, int[][] path) {
        int n = a.length;
        int NOT_A_VERTEX = -1;

        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                d[i][j] = a[i][j]
                path[i][j] = NOT_A_VERTEX;
            }
        }

        for (int k=0; k<n; k++)
            // consider each vertex as an intermediate
            for (int i=0; i<n; i++) 
                for (int j=0; j<n; j++) 
                    if (d[i][k] + d[k][j] < d[i][j]) {
                        d[i][j] = d[i][k] + d[k][j];
                        path[i][j] = k;
                    }
    }

    void dfs(Vertex v) {
        /*
        PERFORM SOME ACTION ON VERTEX HERE
        */

        v.visited = true;
        for (Vertex w : v.adj) 
            if (!w.visited)
                dfs(w);
    }

    //     private boolean dfs() {
    //     /*
    //     Performs a depth-first-search of the activity-node graph
    //     and constructs a (not necessarily the only) topological
    //     ordering of the tasks. If a backward edge is detected,
    //     the graph is cyclic and the project is not realizable.
    //     */
    //     HashMap<Task,Task> parent = new HashMap<Task,Task>();
    //     for (Task s : tasks) {
    //         if (!parent.containsKey(s)) {
    //             parent.put(s, null);
    //             parent = dfsVisit(parent, s);
    //             if (parent == null) {
    //                 // Current node is part of a cycle
    //                 System.out.println(" <- " + s.name);
    //                 return false;
    //             }
    //         }
    //     }
    //     return true;
    // }

    // private HashMap<Task,Task> dfsVisit (HashMap<Task,Task> parent, Task s) {
        
    //     Recursive depth-first search starting at a given node,
    //     if a cycle is detected, the recursion is broken and null
    //     is returned.
        
    //     s.active = true;    // Mark current node as active
    //     // Loop over all edges
    //     for (TEdge e : s.outEdges) {
    //         Task t = e.task;
    //         if (t.active) {
    //             // An active node has been hit: a cycle is detected
    //             System.out.println("Project is not realizable, cycle:");
    //             System.out.print(t.name);
    //             return null;
    //         }
    //         if (!parent.containsKey(t)) {
    //             // Recursively visit new nodes
    //             parent.put(t, t);
    //             parent = dfsVisit(parent, t);
    //             if (parent == null) {
    //                 // Current node is part of a cycle
    //                 System.out.print(" <- " + t.name);
    //                 return null;
    //             }
    //         }
    //     }
    //     s.active = false;
    //     topologicalOrder.add(s.id);
    //     return parent;
    // }

}


