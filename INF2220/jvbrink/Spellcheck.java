import java.io.*;
import java.util.*;

class FileReader {
	/*
	Class for reading words from a given file into
	a BinarySearchTree.
	*/

	private Scanner scanner;

	FileReader(String filename) {
		// Create Scanner object
		try {
			scanner = new Scanner(new File(filename));
		} catch (IOException e) {
			System.err.println("Error: " + e.getMessage());
		} catch (NoSuchElementException e) {
			System.err.println("Error: " + e.getMessage());
		}
		int k = 0;
	}
	
	public void readIntoTree(BinarySearchTree tree) {
		// Reads all words in the file and inserts them into a given BST
		while (scanner.hasNextLine()) {
			String line = scanner.nextLine();
			String[] words = line.split(" ");
			for (int i=0; i<words.length; i++)
				tree.insert(words[i]);
		}
		scanner.close();
	}
}

class SimilarWords {
	public static String[] similarOne(String word) {
		// Words identical to X, but swapped to adjacent characters
		// Method taken from assignment text
		char[] chars = word.toCharArray();
		char[] tmp;
		
		String[] similars = new String[chars.length-1];
		
		for (int i=0; i < chars.length - 1; i++) {
			tmp = chars.clone();
			similars[i] = swap(i, i+1, tmp);
		}
		return similars;
	}

	private static String swap(int a, int b, char[] chars) {
		char tmp = chars[a];
		chars[a] = chars[b];
		chars[b] = tmp;

		return new String(chars);
	}

	public static String[] similarTwo(String word) {
		// Word identical to X, except one letter has been replaced
		char[] chars = word.toCharArray();
		char[] alphabet = "abcdefghijklmnopqrstuvwxyzæøå".toCharArray();
		char[] tmp;
		String[] similars = new String[chars.length*28];
		int k = 0;

		for (int i=0; i<chars.length; i++) {
			for (char c : alphabet) { 
				if (chars[i] != c) {
					tmp = chars.clone();
					tmp[i] = c;
					similars[k++] = new String(tmp);
				}
			}
		}
		return similars;
	}	

	public static String[] similarThree(String word) {
		// Word identical to X, except one letter has been removed
		char[] chars = word.toCharArray();
		char[] alphabet = "abcdefghijklmnopqrstuvwxyzæøå".toCharArray();
		String[] similars = new String[(chars.length+1)*29];
		char[] tmp = new char[chars.length+1];
		int k = 0;

		for (int i=0; i<chars.length+1; i++) {
			for (int j=0; j<chars.length; j++) {
				if (j < i)
					tmp[j] = chars[j];
				else
					tmp[j+1] = chars[j];
			}
			for (char c : alphabet) {
				tmp[i] = c;
				similars[k++] = new String(tmp);
			}
		}
		return similars;
	}

	public static String[] similarFour(String word) {
		// Word identical to X, except one letter has been added
		char[] chars = word.toCharArray();
		String[] similars = new String[chars.length];
		char[] tmp = new char[chars.length-1];

		for (int i=0; i<chars.length; i++) {
			for (int j=0; j<chars.length-1; j++) {
				if (j<i)
					tmp[j] = chars[j];
				else
					tmp[j] = chars[j+1];
			}
			similars[i] = new String(tmp);
		}
		return similars;
	}

	public static HashSet allSimilars(String word) {
		String[] a = similarOne(word);
		String[] b = similarTwo(word);
		String[] c = similarThree(word);
		String[] d = similarFour(word);

		HashSet<String> similars = new HashSet<String>();
		
		int k=0;
		for (int i=0; i<a.length; i++)
			similars.add(a[i]);
		for (int i=0; i<b.length; i++)
			similars.add(b[i]);
		for (int i=0; i<c.length; i++)
			similars.add(c[i]);
		for (int i=0; i<d.length; i++)
			similars.add(d[i]);

		return similars;
	}
}

class Spellcheck {
	public static void main(String[] args) {
		// Create an empty BST		
		BinarySearchTree tree = new BinarySearchTree();

		// Fill the BST with words from file
		String filename = new String("ordbok1_utf.txt");
		FileReader reader = new FileReader(filename);
		reader.readIntoTree(tree);

		// Remove and re-insert the word "familie"
		tree.remove("familie");
		tree.insert("familie");

		// Print out information about the resulting BST
		System.out.println("\nINF2220 Mandatory Exercise 1");
		System.out.println("***Spell Checker***\n");
		System.out.println("File '" + filename + "' has been read into a BST.");
		System.out.println("-------------------------------------------------");
		System.out.println("Number of words: " + tree.size());
		System.out.println("Depth of tree:   " + tree.height());

		int[] depths = tree.depthArray();
		double average_depth = 0;
		for (int i=0; i < depths.length; i++) 
	    	average_depth += i*depths[i];
		average_depth /= tree.size();
		
		System.out.format("Avg. node depth: %.2f%n", average_depth);
		
		System.out.println("Number of nodes at a given depth: ");
		for (int i=0; i < depths.length; i++)
	    	System.out.format("          Depth: %2d  Num. of Nodes: %4d%n", i, depths[i]);
		
		System.out.println("Minimum in tree: " + tree.findMin());
		System.out.println("Maximum in tree: " + tree.findMax());
		System.out.println("-------------------------------------------------");

		// Spell Checking Loop
		System.out.println("\nInitiating Spell Checker\n...");
		String word = new String();
		Scanner scanner = new Scanner(System.in);
		HashSet<String> similars;
		int positive = 0;
		int total = 0;

		while (true) {
			System.out.print("Please enter a single word for lookup (write q to exit): ");

			word = scanner.next();

			if (word.equals("q")) {
				System.out.println("...\nQuitting Spell Checker");
				System.exit(0);
			}
			
			System.out.println("Results: ");

			if (tree.contains(word)) {
				System.out.println(word + " is found in dictionary and spelled correctly.");
				System.out.println((++positive) + " of " + (++total) + " lookups have been found.\n");
			} else {
				System.out.println(word + " is NOT found in dictionary.");
				System.out.println(positive + " of " + (++total) + " lookups have been found.");
				
				System.out.println("Perhaps you meant to write one of these words:");


				similars = SimilarWords.allSimilars(word);
				boolean similarflag = true;

				for (String similarWord : similars)
					if (tree.contains(similarWord)) {
						System.out.println("----> " + similarWord);
						similarflag = false;
					}

				if (similarflag)
					System.out.println("----> No similar words found.");
				System.out.println(" ");
			}
		}
	}
}