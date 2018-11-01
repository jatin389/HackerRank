# https://www.hackerrank.com/contests/projecteuler/challenges/euler002/copy-from/1311196577

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    a=1
    b=1
    sum=0
    c=0
    
    while(c<=n):
        if(c%2==0):
            sum+=c
        c=a+b
        a=b
        b=c
        
    print(sum)
        
