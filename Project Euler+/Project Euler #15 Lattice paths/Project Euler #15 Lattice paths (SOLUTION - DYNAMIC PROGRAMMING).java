// https://www.hackerrank.com/contests/projecteuler/challenges/euler015/copy-from/1311183720


import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        
        while(t>0)
        {
            t--;
            int n=sc.nextInt();
            int m=sc.nextInt();

            int[][] ar=new int[n+1][m+1];

            for(int i=0;i<n+1;i++)
                ar[i][0]=1;

            for(int i=0;i<m+1;i++)
                ar[0][i]=1;

            for(int i=1;i<=n;i++)
            {
                for(int j=1;j<=m;j++)
                {
                    ar[i][j]=(ar[i-1][j]+ar[i][j-1])%1000000007;
                }
            }

            System.out.println(ar[n][m]);
        }
   
    }
}