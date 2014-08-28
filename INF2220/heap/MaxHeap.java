public class MaxHeap {
	private static int[] a;
	private static int n;
	private static int left;
	private static int right;
	private static int largest;


	private static void build_max_heap() {
		n = a.length-1;

		for (int i=n/2; i>=0; i--)
			max_heapify(i);
	}

	private static void max_heapify(int i) {
		left = 2*i;
		right = 2*i+1;
		
		largest = (left  <= n && a[left]  > a[i]) 		? left : i;
		largest = (right <= n && a[right] > a[largest]) ? right : largest;

		if (largest != i) {
			exchange(i, largest);
			max_heapify(largest);
		}
	}

	private static void exchange(int i, int j) {
		int tmp = a[i];
		a[i] = a[j];
		a[j] = tmp;
	}

	public static void HeapSort(int[] array) {
		a = array;
		build_max_heap();
		sort();
	}

	private static void sort() {
		for (int i=n; i > 0; i--) {
			// Place biggest element to the back
			exchange(0,i);
			// Reduce heap size
			n = n-1;
			// Fix heap property
			max_heapify(0);
		}
	}
}

class Starter {
	public static void main(String[] args) {
		int[] a = {7, 3, 2, 4, 16, 5, 9, 12, 11, 21, 6};

		MaxHeap.HeapSort(a);

		for (int i=0; i<a.length; i++)
			System.out.println(a[i]);
	}
}


/*
For a MinHeap class

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

	private void enlargeArray(int size) {
		int[] new_array = new int[size];
		for (int i=0; i<array.length; i++)
			new_array[i] = array[i];

		array = new_array;
	}
*/