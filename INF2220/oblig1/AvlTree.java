import java.util.*;

public class AvlTree {

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
	
	public AvlNode getRoot() {
		return root;
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
			if (height(node.left) - height(node.right) == 2) 
				if (x.compareTo(node.left.key) < 0)
					node = rightRotate(node);
				else
					node = leftRightRotate(node);
		} 

		else if (x.compareTo(node.key) > 0) {
			node.right = insert(x, node.right);
			if (height(node.right) - height(node.left) == 2)
		 		if (x.compareTo(node.right.key) > 0)
					node = leftRotate(node);
				else
			 		node = rightLeftRotate(node);
		}

		node.height = max(height(node.left), height(node.right)) + 1;
		return node;
	}

	private static AvlNode leftRotate(AvlNode x) {
		AvlNode y = x.right;
		x.right = y.left;
		y.left = x;
		return y;
	}

	private static AvlNode rightRotate(AvlNode y) {
		AvlNode x = y.left;
		y.left = x.right;
		x.right = y;
		return x;
	}

	private static AvlNode leftRightRotate(AvlNode z) {
		z.left = leftRotate(z.left);
		return rightRotate(z);
	}

	private static AvlNode rightLeftRotate(AvlNode x) {
		x.right = rightRotate(x.right);
		return leftRotate(x);
	}


	private static int max(int n, int m) {
		return n > m ? n : m;
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

	public void printTree() {
		if (isEmpty())
			System.out.println("The tree is empty.");
		else
			printTree(root);
	}

	private void printTree(AvlNode node) {
		if (node == null)
			return;
		printTree(node.left);
		System.out.println(node.key);
		printTree(node.right);
	}
}



class Starter {
	public static void main(String[] args) {
		AvlTree tree = new AvlTree();

		tree.insert(41);	
		tree.insert(38);
		tree.insert(21);
		tree.insert(12);
		tree.insert(19);
		tree.insert(8);
	}
}


