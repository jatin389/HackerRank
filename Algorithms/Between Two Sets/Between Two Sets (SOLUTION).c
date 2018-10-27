// https://www.hackerrank.com/challenges/between-two-sets/problem

// lcm of first array
// hcf of 2nd array
// count multiples of lcm which are also a factor of hcf


#include<stdio.h>
#include<limits.h>


int gcd(int a,int b)
{
    if(a==0)
        return b;
    return gcd(b%a,a);
}



int main()
{
    int n,m;
    scanf("%d %d",&n,&m); 
    int arr1[n],arr2[m];
    
    int lcm_arr1=1;
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr1[i]);
        lcm_arr1=lcm_arr1*arr1[i]/gcd(lcm_arr1,arr1[i]);
    }

    
    
    scanf("%d",&arr2[0]);
    int hcf_arr2=arr2[0];
    for(int i=1;i<m;i++)
    {
        scanf("%d",&arr2[i]);
        hcf_arr2=gcd(hcf_arr2,arr2[i]);
    }
    
  
    int c=0;
        
   n=lcm_arr1;
    while(n<=hcf_arr2)
    {
        if(hcf_arr2%n==0)
            c++;
        n+=lcm_arr1;
    }
    
    printf("%d",c);
 //   printf("\n%d %d %d",lcm_arr1,hcf_arr2,hcf);
}

