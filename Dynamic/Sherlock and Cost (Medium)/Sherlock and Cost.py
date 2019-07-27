## https://www.hackerrank.com/challenges/sherlock-and-cost/problem

############## BASIC IDEA ###################
# --For 'S' to be largest 'A[i]' will either be '1' or 'B[i]'.
# --DP[i][0] stores the maximum value of 'S' using the first 'i' elements only if A[i] was 1.
# --If A[i] = B[i], then DP[i][1] stores the maximum value of 'S' possible using the first 'i' elements only.
#############################################

t=int(input())
for tt in range(t):
    n=int(input())
    arrB=list(map(int,input().split()))
    dpSum=[[0,0]for i in range(n)]

    for i in range(1,n):
        x=dpSum[i-1][0]+abs(1-1)
        y=dpSum[i-1][1]+abs(arrB[i-1]-1)
        dpSum[i][0]=max(x,y)

        x=dpSum[i-1][0]+abs(arrB[i]-1)
        y=dpSum[i-1][1]+abs(arrB[i]-arrB[i-1])
        dpSum[i][1]=max(x,y)

    ans=max(dpSum[n-1][0],dpSum[n-1][1])
    print(ans)