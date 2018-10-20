# https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence/problem

i1,i2=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

ar=[[0 for i in range(len(a)+1)] for j in range(len(b)+1)]


for i in range(1,len(b)+1):
    for j in range(1,len(a)+1):
        x=0
        if(b[i-1]==a[j-1]):
            x=ar[i-1][j-1]+1
        
        ar[i][j]=max(x,ar[i-1][j],ar[i][j-1])
      
    
    
# tracing the sequence
i=len(b)
j=len(a)
ans=[]
while(i and j):
    if(ar[i][j]==ar[i-1][j]):
        i-=1
    elif(ar[i][j]==ar[i][j-1]):
        j-=1
    else:
        ans.append(b[i-1])
        i-=1
        j-=1
        
for i in reversed(ans):
    print(i)
    

