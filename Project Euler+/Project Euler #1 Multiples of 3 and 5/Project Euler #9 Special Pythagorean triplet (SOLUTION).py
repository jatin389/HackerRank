# https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem

# BASIC idea:
# Calculate sum of A.P. series 
# 3*5=15
# Therefore, ans=sumofAP(3)+sumofAP(5)-sumofAP(15)


def AP_sum(a,n):
    return(n*(2*a+(n-1)*a)//2)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    a=(n-1)//3
    b=(n-1)//5
    c=(n-1)//15
    
    sum_a = AP_sum(3,a)
    sum_b = AP_sum(5,b)
    sum_c = AP_sum(15,c)
    
    print(sum_a + sum_b - sum_c)
    
    
