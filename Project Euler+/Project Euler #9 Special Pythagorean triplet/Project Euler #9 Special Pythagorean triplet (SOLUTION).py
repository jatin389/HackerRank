# https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem

# solve 2 equations
# 1. a+b+c=n
# 2. a^2 + b^2 = c^2
# we have a & n - solve for b & c



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    res=0
    
    
    for a in range(1,(n//2+1)):
        x=a*a + (n-a)*(n-a)
        y=2*(n-a)
        c=(x/y)
        if(c!=int(c)):                  # because we dont want decimal values
            continue
        b=(n-a)-c
        
        tmp=int(a*b*c)
        res=max(res,tmp)
        
    if(res==0):
        res=-1
    print(res)
        
