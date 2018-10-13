# https://www.hackerrank.com/contests/projecteuler/challenges/euler008/copy-from/1310912248


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    lst=list(str(num))
    
    mul=1
    
    for i in range(k):
        mul*=int(lst[i])
        
    tmp=mul
    for i in range(k,n):
        try:
            tmp/=int(lst[i-k])
            tmp*=int(lst[i])
      #      print("..............." , lst[i-k] , lst[i], mul , tmp)
        except:
            tmp=1
            for i in range(i-k+1,i+1):
                tmp*=int(lst[i])
        
        
        mul=max(mul,tmp)
    print(int(mul))
    
