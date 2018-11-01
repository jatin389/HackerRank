# https://www.hackerrank.com/contests/projecteuler/challenges/euler003/copy-from/1311210329


import math

def fun(n): 
    while(n%2==0):
            n=n//2
    if(n==1):
        return 2
    
    i=3
    ans=3
    n1=int(math.sqrt(n))+1
    
    while(n>1 and i<=n1):
        if(n%i==0):
            n=n//i
            ans=i
        else:
            i+=2
    
    if(n!=1):
        return n
    else:
        return ans
    


    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(fun(n))
    
    
            
        
