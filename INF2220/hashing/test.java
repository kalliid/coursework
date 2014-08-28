class HashTable {
	int m; // size of table

	public void insert(Element item) {
		// Inserts an item into the hashtable
	}

	public void remove(Element item) {
		// Removes an item from the hashtable
	}

	public Element find(Element item) {
		// Return element if found, none else
	}

	private int prehash(String s) {
		// computes a non-negative key for a given string
	}

	private int hash(int key) {
		// computes a hash in [0, 1, ..., m-1] from a given key
	}

	private class Node {
		Element item;
		int key;
		Node next;
	}




}