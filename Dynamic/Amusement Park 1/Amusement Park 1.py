# https://www.hackerrank.com/contests/codeit-14/challenges/amusement-park-1

n=int(input().strip())

arr=[[] for i in range(n)]
for i in range(n):
    arr[i]=list(map(int,input().strip().split()))
    
ans=[[1]*n for i in range(n)]

ans[0][0]=arr[0][0]

for i in range(1,n):
    ans[0][i]=max(ans[0][i-1],arr[0][i])
    ans[i][0]=max(ans[i-1][0],arr[i][0])

for i in range(1,n):
    for j in range(1,n):
        x=min(ans[i][j-1],ans[i-1][j])
        ans[i][j]=max(arr[i][j],x)
print(ans[n-1][n-1])
