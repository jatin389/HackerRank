# https://www.hackerrank.com/challenges/flipping-the-matrix/problem


q=int(input())
for q0 in range(q):
    n=int(input())
    ar=[]
    for i in range(2*n):
        ar.append(list(map(int,input().strip().split())))
    
    res=0
    
    for i in range(n):
        for j in range(n):
            dist_row=n-i
            dist_col=n-j
            
            res+=max(ar[i][j],ar[i][j+2*dist_col-1],ar[i+2*dist_row-1][j],ar[i+2*dist_row-1][j+2*dist_col-1])
            
    print(res)
    
