# https://www.hackerrank.com/challenges/new-year-chaos/problem


# More optimised solution
# with reduced range



def minimumBribes(q):
    for i in range(1,len(q)+1):
        if(q[i-1] > i+2):
            return ("Too chaotic")
    
    count = 0
    for i in range(len(q)-1,-1,-1):                     # reverse traversal
        for j in range(max(0, q[i] - 2),i):             # to reduce range - because any element at 'k'th position can swap atmost 2 elements in front of it.
                                                        # Hence, the range should be (element(i)-2 till i)
            if q[j] > q[i]:
                count+=1
    return(count)
    



    

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        x=minimumBribes(q)
        print(x)
