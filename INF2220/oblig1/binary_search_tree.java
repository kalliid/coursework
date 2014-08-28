import java.util.*;

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
		int height; 	// Lar høyden
	
		Node(Comparable key) {
			this(key, null, null);
		}
	
		Node(Comparable k, Node l, Node r) {
			key = k; left = l; right = r; height = 0;
		}
	}

	private Node root;

	BinarySearchTree() {
		root = null;
	}


	public void insert(Comparable x) {
		// Inserts into tree, duplicates are ignored
		root = insert(x, root);
	}

	private Node insert(Comparable x, Node node) {
		// Recursive insertion method 
		if (node == null)
			node = new Node(x);
		else if (x.compareTo(node.key) < 0)
			node.left = insert(x, node.left);
		else if (x.compareTo(node.key) > 0)
			node.right = insert(x, node.right);
		
		node.height = max(height(node.left), height(node.right)) + 1;
		return node;		
	}

	private static int max(int n, int m) {
		return n > m ? n : m;
	}

	private static int height(Node node) {
		// Returns height of a node, height of a null node is defined to be -1
		return node == null ? -1 : node.height;
	}

	private Comparable key(Node node) {
		return node == null ? null : node.key;
	}

	public void makeEmpty() {
		root = null;
	}

	public boolean isEmpty() {
		return (root == null);
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
}


class Starter {
	public static void main(String[] args) {
		BinarySearchTree tree = new BinarySearchTree();

		tree.insert(41);	
		tree.insert(38);
		tree.insert(21);
		tree.insert(12);
		tree.insert(19);
		tree.insert(8);

		tree.printTree();
	}
}






/*


import java.util.*;

class BinarySearchTree {

	private class BinaryNode {
		Integer value;
		BinaryNode left;
		BinaryNode right;
		BinaryNode parent;

		BinaryNode(Integer value, BinaryNode left, BinaryNode right) {
			this.value = value;
			this.left = left;
			this.right = right;
		}

		BinaryNode(Integer value) {
			this(value, null, null);
		}
	}

	private BinaryNode root;

	BinarySearchTree() {
		root = null;
	}

	public void makeEmpty() {
		root = null;
	}

	public boolean isEmpty() {
		return (root == null);
	}

	public boolean contains(Integer x) {
		BinaryNode current = root;

		while (current != null) {
			Integer compareResult = x.compareTo(current.value);
		
			if (compareResult == 0)
				return true;
			else if (compareResult < 0)
				current = current.left;
			else
				current = current.right;

		}

		return false;
	}

	public void insert(Integer x) {
		BinaryNode current = root;
		BinaryNode newNode = new BinaryNode(x);

		if (root == null) {
			root = newNode;
		}

		while (current != null) {
			Integer compareResult = x.compareTo(current.value);

			if (compareResult == 0) {
				System.out.println(x + " already contained in tree!");
				return;
			}

			if (compareResult < 0) {
				if (current.left == null) {
					current.left = newNode;
					return;
				} else {
					current = current.left;
				}
			} else if (compareResult > 0) {
				if (current.right == null) {
					current.right = newNode;
					return;
				} else {
					current = current.right;
				}
			}
		}
	}

	public void remove(Integer x) {
		root = remove(x, root);
	}

	private BinaryNode remove(Integer x, BinaryNode node) {
		if (node == null)
			return null;

		int compareResult = x.compareTo(node.value);

		if (compareResult < 0)
	 		node.left = remove(x, node.left);
	 	else if (compareResult > 0)
	 		node.right = remove(x, node.right);
	 	else if (node.left != null && node.right != null) {
	 		node.value = findMin(node.right).value;
	 		node.right = remove(node.value, node.right);
	 	}
	 	else
	 		node = (node.left != null) ? node.left : node.right;

	 	return node;
	}

	public int size() {
		if (root == null)
			return 0;
				
		return size(root.left) + size(root.right) + 1;
	}

	private int size(BinaryNode node) {
		if (node == null)
			return 0;
		else
			return size(node.left) + size(node.right) + 1;
	}

	public int findMin() {
		return findMin(root).value;
	}

	public int findMax() {
		return findMax(root).value;
	}

	private BinaryNode findMin(BinaryNode node) {
		if (node != null)
			while (node.left != null)
				node = node.left;
		return node;
	}

	private BinaryNode findMax(BinaryNode node) {
		if (node != null)
			while (node.right != null)
				node = node.right;
		return node;
	}

	public void printTree() {
		if (root == null)
			return;

		if (root.left != null)
			printTree(root.left);

		System.out.println(root.value);
		
		if (root.right != null)
			printTree(root.right);
	}

	private void printTree(BinaryNode node) {
		if (node.left != null)
			printTree(node.left);
		System.out.println(node.value);
		if (node.right != null)
			printTree(node.right);
	}
}


class Starter {
	public static void main(String[] args) {
		BinarySearchTree tree = new BinarySearchTree();
		System.out.println(tree.isEmpty() + " true");
		System.out.println(tree.size() + " 0");
		tree.insert(4);
		System.out.println(tree.size() + " 1");
		System.out.println(tree.isEmpty() + " false");
		System.out.println(tree.contains(3) + " false");
		System.out.println(tree.contains(4) + " true");

		tree.insert(2);
		tree.insert(-3);
		tree.insert(12);
		tree.insert(6);
		tree.insert(10);
		System.out.println(tree.contains(2) + " true");
		System.out.println(tree.contains(7) + " false");
		System.out.println(tree.contains(10) + " true");
		System.out.println(tree.contains(-3) + " true");
		System.out.println(tree.size() + " 6");

		System.out.println(tree.findMin() + " -3");
		System.out.println(tree.findMax() + " 12");


		tree.printTree();
	}
}
*/