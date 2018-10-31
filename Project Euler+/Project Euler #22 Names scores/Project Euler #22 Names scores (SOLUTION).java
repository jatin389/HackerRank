// https://www.hackerrank.com/contests/projecteuler/challenges/euler022/copy-from/1311194275


import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        
        TreeSet<String> ts=new TreeSet<String>();
        int n=Integer.parseInt(br.readLine());
               
        for(int nn=0;nn<n;nn++)
            ts.add(br.readLine());
       
   
        
        int q=Integer.parseInt(br.readLine());
        while(q>0)
        {
            q--;
            String str=br.readLine();
            
            int value=0;
            for(int i=0;i<str.length();i++)
                value+=str.charAt(i)-64;
            
            int i=1;
            for(String s: ts)
            {
                if(str.equals(s))
                    break;
                i++;
            }
            
            System.out.println(value*i);            
        }    
    }
}