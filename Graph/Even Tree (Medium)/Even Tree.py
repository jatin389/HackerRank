## https://www.hackerrank.com/challenges/even-tree/problem


######### BASIC IDEA #######################
# count no. of child nodes (recurrsively)
# if odd no. of childs: 
#     then break the edge
#     and increse ANS by 1
#     return '0' -- representing no child(after separation)
# else:
#     return no. of childs + 1
#############################################


nodes,edges=map(int,input().split())
graph={i:[] for i in range(1,nodes+1)}

for i in range(edges):
    vertexi,vertexj=map(int,input().split())
    graph[vertexi].append(vertexj)
    graph[vertexj].append(vertexi)

####### convert graph to tree ############
####### converting bidirection to unidirectional graph #########
visited=[0 for i in range(nodes+1)]
tmpQueue=[1]
while(len(tmpQueue)>0):
    key=tmpQueue.pop()
    visited[key]=1
    tmp=[]
    for elem in graph[key]:
        if(visited[elem]==0):
            tmp.append(elem)
    tmpQueue+=tmp
    graph[key]=tmp
##############################################3

ANS=0
def DFS(root):
    global graph
    global ANS
    tmp=[]
    tmp=graph[root]
    if(len(tmp)==0):
        return 1
    sumOfChildVertices=0
    for child in tmp:
        sumOfChildVertices+=DFS(child)

    if(sumOfChildVertices+1)%2==0:
        ANS+=1
        return 0
    return (sumOfChildVertices+1)
    
DFS(1)
print(ANS-1)