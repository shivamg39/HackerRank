import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        ArrayList<String> as = new ArrayList<String>();
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext()) {
            String s = scan.nextLine();
            as.add(s);
        }
        for (int i = 1; i <= as.size(); i++) {
            System.out.println(i +" "+ as.get(i-1));
        }
    }
}










