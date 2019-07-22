## https://www.hackerrank.com/challenges/the-quickest-way-up/problem


############# BASIC IDEA ############
# 1. Assume each cell as a node in a graph
# 2. for ladders and destination:
#         sourceNode=destinationNode          --- hence eliminate source node
# 3. Apply BFS - with each node can have atmost 6 adjacent nodes
# 4. replace SourceNode with DestNode --in case of cell contains snake/ladder startpoint 
#######################################

def BFS(n):
    visited=[0 for i in range(101)]
    visited[1]=1
    count=0
    BFSQueue=[(n,count)]
    while(len(BFSQueue)>0):
        # print(BFSQueue)
        tmp=BFSQueue.pop()
        helperArr=[]
        count=tmp[1]
        count+=1
        for i in range(1,7):
            x=tmp[0]+i
            if(x==100):
                return count
            if(x<100):
                x=Snake_Ladder[x] 
                if(x==100):
                    return count
                if(visited[x]==0):
                    visited[x]=1
                    helperArr.append((x,count))
        BFSQueue=helperArr+BFSQueue
    return -1

t=int(input())
for testCase in range(t):
    Snake_Ladder=[i for i in range(101)]
    ladders=int(input())
    for i in range(ladders):
        source,dest=map(int,input().split())
        Snake_Ladder[source]=dest
    snakes=int(input())
    for i in range(snakes):
        source,dest=map(int,input().split())
        Snake_Ladder[source]=dest

    print(BFS(1))                               
