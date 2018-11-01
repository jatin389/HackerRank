# https://www.hackerrank.com/contests/projecteuler/challenges/euler002/copy-from/1311196577

# f(n)=4*f(n-1) + f(n-2)

def fib(n):
    i=1
    sum=0

    f0=2
    f1=8
    f2=0

    while(f1<=n):
        sum+=f1

        f2=4*f1+f0
        f0=f1
        f1=f2

    return (sum+2)


t=int(input())
for tt in range(t):
    n=int(input())
    print(fib(n))
        
