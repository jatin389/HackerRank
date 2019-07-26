## https://www.hackerrank.com/challenges/equal/copy-from/116079870

import math
t=int(input())
for tt in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    operations=[5,2,1]
    mini=min(arr)+1    
    ans=math.inf
    for k in range(5):
        count=0
        mini-=1
        for i in arr:
            for j in operations:
                if((i-mini)>=j):
                    tmp=(i-mini)//j
                    i-=tmp*j
                    count+=tmp  
        ans=ans if(ans<count) else count              

    print(ans)
