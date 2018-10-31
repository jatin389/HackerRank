# https://www.hackerrank.com/contests/projecteuler/challenges/euler015/copy-from/1311183836


def fact(n):
    f=1
    while(n>1):
        f*=n
        n-=1   
    return f



t=int(input())
for tt in range(t):
    m,n=map(int,input().split())
    print((fact(m + n) // (fact(m) * fact(n))) % 1000000007)



