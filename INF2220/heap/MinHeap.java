public class MinHeap {
	int[] array;
	int n;

	public void insert(int x) {
		if (n == array.length - 1)
			enlargeArray(array.length*2 + 1);

		// Hole is generated at end of array
		int hole = ++n;

		// Percolate up
		for (array[0] = x; x < array[hole/2]; hole /= 2)
			array[hole] = array[hole/2];
		
		// Insert new element
		array[hole] = x;
	}

	public int extractMin() {
		// Save the root
		array[0] = array[1];
		// Replace the root with last element
		array[1] = array[n--];
		// Percolate down new root
		percolateDown(1);

		return array[0];
	}

	private void percolateDown(int hole) {
		int child;
		int tmp = array[hole];

		for (; hole * 2 <= n; hole=child) {
			
		}

	}

	private void enlargeArray(int size) {
		int[] new_array = new int[size];
		for (int i=0; i<array.length; i++)
			new_array[i] = array[i];

		array = new_array;
	}
}