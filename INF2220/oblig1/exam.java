class Exam_BST {
    Node root;

    class Node {
        int key;
        Node left;
        Node right;

        Node(int n, Node l, Node r) {
            key = n;
            left = l;
            right = l;
        }

        Node(int n) {
            this(n, null, null);
        }
    }

    public int min_key() {
        return min_key(root);
    }

    private int min_key(Node n) {
        if (n==null)
            return Integer.MAX_VALUE;
        else
            return min(min_key(n.left), min_key(n.right));
    }

    public int max_key() {
        return max_key(root);
    }

    private int max_key(Node n) {
        if (n==null)
            return 0;
        else
            return max(max_key(n.left), max_key(n.right), n.key);
    }

    private int min(int i, int j, int k) {
        return min(min(i, j), k);
    }

    private int min(int m, int n) {
        return m < n ? m : n;
    }

    private int max(int m, int n) {
        return m > n ? m : n;
    }

    public boolean is_bst() {
        return is_bst(root);
    }

    private boolean is_bst(Node n) {
        if (n == null)
            return true;
        
        if (!is_bst(n.left) || !is_bst(n.right))
            return false;

        return (max_key(n.left) < n.key && n.key < min_key(n.right));
    }
    
    public boolean is_bst() {
        return is_bst_help(root, Integer.MAX_VALUE, 0);
    }   

    private boolean is_bst_help(Node n, int low, int high) {
        if (n.value > low || n.value < high)
            return false;
        
        return (is_bst_help(n.left, n.value, high) && is_bst_help(n.right, low, n.value));
    }
}

