# https://www.hackerrank.com/contests/projecteuler/challenges/euler005/copy-from/1311193329

# ans = LCM of array

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    lcm=1
    for i in range(2,n+1):
        lcm=(i*lcm)//(gcd(i,lcm))
        
    print(lcm)
