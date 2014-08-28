//import java.util.*;

class BinarySearchTree {
	/*
	Class for a binary search tree storing a Comparable object,
	supporting insertion, removal and traversal.
	Tree is NOT self-balancing.
	*/

	private class Node {
		Comparable key; // value of the node
		Node left;		// root of left subtree
		Node right; 	// root of right subtree
		int height; 	// height of the node
		int depth;		// depth of the node
	
		Node(Comparable k, int d) {
			key = k;
			left = null;
			right = null;
			height = 0;
			depth = d;
		}
	}

	private Node root;

	BinarySearchTree() {
		root = null;
	}
	
	public void makeEmpty() {
		// Deletes the tree
		root = null;
	}

	public boolean isEmpty() {
		return (root == null);
	}

	public void insert(Comparable x) {
		// Inserts into tree, duplicates are ignored
		root = insert(x, root, 0);
	}

	private Node insert(Comparable x, Node node, int d) {
		// Recursive insertion method 
		if (node == null)
			node = new Node(x, d);
		else if (x.compareTo(node.key) < 0)
			node.left = insert(x, node.left, d+1);
		else if (x.compareTo(node.key) > 0)
			node.right = insert(x, node.right, d+1);
		
		node.height = max(height(node.left), height(node.right)) + 1;
		return node;		
	}

	public boolean contains(Comparable x) {
		// Returns true if a node with key x exists in tree
		return contains(x, root);
	}

	private boolean contains(Comparable x, Node node) {
		if (node == null) 
			return false;

		if (x.compareTo(node.key) == 0)
			return true;
		else if (x.compareTo(node.key) < 0)
			return contains(x, node.left);
		else
			return contains(x, node.right);
	}

	private static int max(int n, int m) {
		return n > m ? n : m;
	}

	public int size() {
		return size(root);
	}

	private int size(Node node) {
		if (node == null)
			return 0;
		return size(node.left) + size(node.right) + 1;
	}

	private Comparable key(Node node) {
		return node == null ? null : node.key;
	}

	public Comparable findMin() {
		// Find smallest key in tree
		return key(findMin(root));
	}

	public Comparable findMax() {
		// Find biggest key in tree
		return key(findMax(root));
	}

	private Node findMin(Node node) {
		// Recursively find smallest key in subtree with node as root
		if (node == null)
			return node;

		while (node.left != null)
			node = node.left;

		return node;
	}

	private Node findMax(Node node) {
		// Recursively find biggest key in subtree with node as root
		if (node == null)
			return node;

		while (node.right != null)
			node = node.right;

		return node;
	}

	public int height() {
		return height(root);
	}

	private static int height(Node node) {
		// Returns height of a node, height of a null node is defined to be -1
		return node == null ? -1 : node.height;
	}

	public void printTree() {
		if (isEmpty())
			System.out.println("The tree is empty.");
		else
			printTree(root);
	}

	private void printTree(Node node) {
		if (node == null)
			return;
		printTree(node.left);
		System.out.println(node.key);
		printTree(node.right);
	}

	public int[] depthArray() {
	 	// Returns an array of length equal to the tree's height,
	 	// where each element indicates how many nodes have a given depth
	 	if (isEmpty()) {
			System.out.println("The tree is empty.");
			return null;
		}
	 	int[] depths = new int[height()+1];
	 	depths = depthArray(root, depths);
	 	return depths;
	 }

	private int[] depthArray(Node node, int[] depths) {
		// Recursive method to add depths of all nodes in a given subtree
		// order of traversal is inconsequential
		if (node == null)
			return depths;

		depths = depthArray(node.left, depths);
		depths = depthArray(node.right, depths);
		depths[node.depth]++;
		return depths;
	}

	public void remove(Comparable x) {
		// Removes x from the tree if present
		root = remove(x, root);
	}

	private Node remove(Comparable x, Node node) {
		// Removes x from subtree with root node if present
		if (node == null)
			return null;

		if (x.compareTo(node.key) < 0)
			node.left = remove(x, node.left);
		else if (x.compareTo(node.key) > 0)
			node.right = remove(x, node.right);
		else if (node.left != null && node.right != null) {
	 		node.key = findMin(node.right).key;
	 		node.right = remove(node.key, node.right);
	 	} else
	 		node = (node.left != null) ? node.left : node.right;

	 	return node;
	}
}