# https://www.hackerrank.com/challenges/new-year-chaos/problem

# BASIC IDEA: 
# Use Bubble sort
# and return number of swaps




def minimumBribes(q):
    for i in range(1,len(q)+1):
        if(q[i-1] > i+2):
            return ("Too chaotic")
    
    c=0
    n=len(q)

    #Bubble Sort
    for i in range(n-1):
        for j in range(n-i-1):
                if(q[j]>q[j+1]):
                    q[j],q[j+1]=q[j+1],q[j]
                    c+=1
                
    return c
    
    


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        x=minimumBribes(q)
        print(x)




