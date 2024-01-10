# Task 1(b)
# Topological sort BFS

from queue import Queue
q = Queue()

inputFile=open('Lab5_input1(b).txt','r')
out=open('Lab5_output(b).txt','w')

nodes, edges = map(int, inputFile.readline().split())
graph_dict = {}

for i in range(1, nodes + 1):
    graph_dict[i] = []

indegree = [0] * (nodes + 1)
for i in range(edges):
    u, v = map(int, inputFile.readline().split())
    graph_dict[u].append(v)
    indegree[v]+=1  # Extra part for BFS

path = []
# cycle = False
# red = [0]*(nodes+1) #visit start
# blue = [0]*(nodes+1) #processing
#
# def Cycle_Check(u):
#     global cycle
#     red[u]=1 # ekhon process hobe
#     blue[u]=1 #call stack e
#     for v in graph_dict[u]:
#         if red[v]==1:
#             if blue[v]==1:
#                 cycle=True
#         else:
#             Cycle_Check(v)
#     blue[u]=0
#
# for i in range(1, int(nodes)+1):
#     if not cycle:
#         Cycle_Check(i)

col=['White']*(nodes+1)

visited=False

def Cycle_Check(G,s): # modified DFS for cycle checking
    global time
    global visited
    col[s]='Grey' #processing

    for u in G[s]:
        if col[u]=='White': #visit start
            Cycle_Check(G,u)
        elif col[u]=='Grey':
            visited=True
    col[s]='Black'

def BFS(G):
    for i in range(1, nodes + 1):
        if indegree[i] == 0:
            q.put(i)
    while not q.empty():
        u = q.get()
        path.append(u)
        for v in G[u]:
            indegree[v]-=1 #This is because we have processed u, and it contributes to the in-degree reduction of its neighbors.
            if indegree[v]==0:
                q.put(v)

if visited:
    out.write('IMPOSSIBLE')
else:
    BFS(graph_dict)

for i in path:
    out.write(f'{i} ')
