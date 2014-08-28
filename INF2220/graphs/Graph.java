public class Graph() {
	Node[] nodes;

	private class Node() {
		Edge adj;
		int value;

		Node() {
			adj = null;
		}

		private class Edge() {
			Edge next;
			Node neighbor;
		}
	}
}