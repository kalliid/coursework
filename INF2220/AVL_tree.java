import java.util.*;

class AvlTree {

	private class AvlNode {
		Comparable  key;
		AvlNode 	left;
		AvlNode		right;
		int 		height;

		AvlNode(Comparable key) {
			this(key, null, null);
		}

		AvlNode(Comparable k, AvlNode l, AvlNode r) {
			key 	= k;
			left 	= l;
			right 	= r;
			height 	= 0;
		}
	}

	private AvlNode root;

	public AvlTree() {
		root = null;
	}
	
	public void insert(Comparable x) {
		// Insert into tree, duplicates are ignored
		root = insert(x, root);
	}


	private AvlNode insert(Comparable x, AvlNode node) {
		if (node == null)
			node = new AvlNode(x);
		
		else if (x.compareTo(node.key) < 0) {
			node.left = insert(x, node.left);
			// MUST BALANCE HERE
		} 

		else if (x.compareTo(node.key) > 0) {
			node.right = insert(x, node.right);
			// MUST BALANCE HERE
		}

		node.height = max(height(node.left), height(t.right)) + 1;
		return node;
	}

	private static int height(AvlNode node) {
		return node == null ? -1 : node.height;
	}

	public Comparable findMin() {
		return key(findMin(root));
	}

	public Comparable findMax() {
		return key(findMax(root));
	}

	private AvlNode findMin(AvlNode node) {
		if (node == null)
			return node;

		while (node.left != null)
			node = node.left;

		return node;
	}

	private AvlNode findMax(AvlNode node) {
		if (node == null)
			return node;

		while (node.right != null)
			node = node.right;

		return node;
	}

	private Comparable key(AvlNode node) {
		return node == null ? null : node.key;
	}

	public void makeEmpty() {
		root = null;
	}

	public boolean isEmpty() {
		return (root == null);
	}
}





/*
	public void remove(Comparable x) {
		// Not implemented
	}


	public void printTree() {
		if (isEmpty())
			return;
		else
			printTree(root);
	}

	private AvlNode insert(Comparable x, AvlNode node) {
		if (node == null)
			node = new AvlNode(x);
		
		else if (x.compareTo(node.key) < 0) {
			node.left = insert(x, node.left)
			// MUST BALANCE HERE
		} 

		else if (x.compareTo(node.key) > 0) {
			node.right = insert(x, node.right);
			// MUST BALANCE HERE
		}

		node.height = max(height(node.left), height(t.right)) + 1;
		return node
	}


	private static int height(AvlNode node) {
		return node == null ? -1 : node.height
	}





import java.util.*;


class AvlTree {

	private class AvlNode {
		Integer key;
		AvlNode left;
		AvlNode right;
		AvlNode parent;

		AvlNode(Integer key) {
			this(value, null, null, null);
		}	

		AvlNode(Integer key, AvlNode parent) {
			this(value, null, null, parent);
		}

		AvlNode(Integer key, AvlNode left, AvlNode right, AvlNode parent) {
			this.key = key;
			this.left = left;
			this.right = right;
			this.parent = parent;
		}
	}


	private AvlNode root;

	AvlTreee() {
		root = null;
	}

	public void makeEmpty() {
		root = null;
	}

	public boolean isEmpty() {
		return (root == null);
	}

	public boolean contains(Integer x) {
		return contains(x, root);
	}


	private boolean contains(Integer x, AvlNode n) {

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
*/

class Starter {
	public static void main(String[] args) {
		AvlTree tree = new AvlTree();
	}
}
