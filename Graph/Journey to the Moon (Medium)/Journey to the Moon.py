## https://www.hackerrank.com/challenges/journey-to-the-moon/problem

n,p=map(int,input().strip().split())
visited=[0 for i in range(n)]
noOfPaths=0                                  # count total number of countries
paths={}                                     # count no. of nodes in a country
graph={i:[] for i in range(n)}

for i in range(p):
    x,y=map(int,input().strip().split())
    graph[x].append(y)
    graph[y].append(x)

BFSQueue=[]
for i in graph.keys():
    if(visited[i]==0):                   # proceed only if node has not been visited yet
        noOfPaths+=1
        BFSQueue.append(i)
        paths[i]=0
        while(len(BFSQueue)>0):         # BFS LOOP
            node=BFSQueue.pop()
            if(visited[node]==0):
                visited[node]=1
                paths[i]+=1
                BFSQueue+=graph[node]

############## till now we have "no of countries" and "no. of nodes in each country"
# Basic Idea:
# TotalNodes - NoOfNodesInCountry       // to get all the other remaining pair-able nodes

# (TotalNodes - NoOfNodesInCountry) * NoOfNodesInCountry    // create pair(or connect edges) with every node of the country
################################################################
ans=0
for country in paths.keys():
    ans+=(n-paths[country])*paths[country]
ans=ans//2                                     # every edge/pair is considered twice
print(ans) 