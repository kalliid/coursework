import java.io.*;
import java.util.*;

class SearchString {
    /*
    Searches a string for a given pattern. Returns a list of the indices
    of all occurences of the substring. The special character '_' is a 
    wildcard, and matches to any char in the text string. If no matches
    are found, an empty list is returned.
    */

    String pattern;
    String text;
    char[] needle;
    char[] haystack;
    int nlen;
    int hlen;
    int last;
    int CHAR_MAX = 65536; // Assume 2-byte chars, java char is UTF-16
    int[] badCharShift = new int[CHAR_MAX];
    int leadingWildcards;

    SearchString(String pattern, String text) {
        this.pattern = pattern;
        this.text = text;
        needle = pattern.toCharArray();
        haystack = text.toCharArray();
        nlen = needle.length;
        hlen = haystack.length;
        last = nlen - 1;

        leadingWildcards = 0;
        for (char c : needle)
            if (c == '_')
                leadingWildcards++;
            else
                break;

        if (nlen == 0)
            System.out.println("Warning: Empty needle, no matches exist");
        else if (nlen > hlen)
            System.out.println("Warning: Needle is bigger than haystack.");
        else if (leadingWildcards == nlen) {
            System.out.println("Warning: Wildcard needle matches everything!");
            leadingWildcards--;
        }
            

        for (int i=0; i<CHAR_MAX; i++)
            badCharShift[i] = nlen - leadingWildcards;

        for (int i=0; i < last; i++)
            badCharShift[needle[i]] = last - i;
    }

    public Integer[] search() {
        /*
        Searches the haystack for all matches of the needle, and
        returns all hits as an array of indicies of the first char
        of every hit.
        */

        List<Integer> hits = new ArrayList<Integer>();
        int offset = 0;
        int maxoffset = haystack.length - needle.length;

        if (nlen == 0 || nlen > hlen) {
            return hits.toArray(new Integer[hits.size()]);
        }

        while (offset <= maxoffset) {
            for (int scan=last; match(scan+offset, scan); scan--) {
                if (scan == leadingWildcards) {
                    hits.add(offset);
                    break;
                }
            }
            offset += badCharShift[haystack[offset + last]];
        }
        return hits.toArray(new Integer[hits.size()]);
    }

    public void print_hits() {
        /*
        Prints all hits in a text in order.
        */
        Integer[] hits = search();

        if (hits.length == 0) {
            System.out.println("No matches found.");
            return;
        }

        for (int i=0; i<hits.length; i++) {
            System.out.print("Index: " + hits[i] + " Match: ");
            for (int j=hits[i]; j<hits[i]+nlen; j++) {
                System.out.print(haystack[j]);
            }
            System.out.print("\n");
        }
    }

    private boolean match(int i, int j) {
        /*
        Checks if the needle character with index j matches the 
        haystack character with index i.
        A wildcard char always matches.
        */
        if (needle[j] == '_')
            // Wildcard match
            return true;
        return (haystack[i] == needle[j]);
    }
}

class SimpleTestRun {
    public static void main(String[] args) {
        String text = "cogwrgaccag";
        System.out.println("Looking at text: " + text + "\n");

        //String patterns[] = {"c_g", "_wr", "_c_", "___"};
        String patterns[] = {"", "c_g", "_wr", "_c_", "___"};
        for (String pattern : patterns) {
            SearchString searcher = new SearchString(pattern, text);
            System.out.println("Matching pattern " + pattern + ":");
            searcher.print_hits();
            System.out.print("\n");
        }

        System.out.println("Test empty haystack: \n");
        SearchString search = new SearchString("a", "");
        search.print_hits();
    }
}

class SearchFile {
    public static void main(String[] args) {
        /*
        Takes an inputfile to be searched and a pattern from the cml,
        any file in UTF-16 is supported. 
        */

        // Read command-line arguments
        if (args.length != 2) {
            String error="InputError, usage: java Oblig2 inputfile pattern";
            System.out.println(error);
            return;
        }

        String inputfile = args[0];
        String text = "";
        Scanner scanner = null;
        try {
            scanner = new Scanner(new File(inputfile));
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        } catch (NoSuchElementException e) {
            System.err.println("Error: " + e.getMessage());
        }
       
       while (scanner.hasNext()) {
            text += scanner.nextLine();
            text += " ";
        }

        String pattern = args[1];
        SearchString searcher = new SearchString(pattern, text);

        System.out.println("Matching pattern '" + pattern + "' to file: " + inputfile);
        searcher.print_hits();
    }
}