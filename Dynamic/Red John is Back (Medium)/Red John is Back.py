## https://www.hackerrank.com/challenges/red-john-is-back/problem

t=int(input().strip())
ans=[0 for i in range(41)]
ans[1]=1
ans[2]=1
ans[3]=1
ans[4]=2

def findNoOfWays():
    for i in range(5,41):
        ans[i]=ans[i-1]+ans[i-4]

def SieveofEratosthenes(n):
    for i in range(2,n+1):
        if(prime[i]==0):
            prime[i]=1
            tmp=i*2
            while(tmp<=n):
                prime[tmp]=-1
                tmp+=i

def countNoOfPrimes(n):
    count=0
    for i in range(1,n+1):
        if(prime[i]==1):
            count+=1
        noOfPrimes[i]=count

########################################
findNoOfWays()
prime=[0 for i in range(ans[40]+1)]
noOfPrimes=[0 for i in range(ans[40]+1)]
SieveofEratosthenes(ans[40])
countNoOfPrimes(ans[40])
for testCase in range(t):
    n=int(input().strip())
    print(noOfPrimes[ans[n]])
    
