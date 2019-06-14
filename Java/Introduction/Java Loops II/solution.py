import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i = 0; i < t; i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int num = a;
            for(int times = 0; times < n; times++) {
                num += Math.pow(2, times) * b; 
                System.out.print(num + " ");
            }
            System.out.println();
        }
        in.close();
    }
}

