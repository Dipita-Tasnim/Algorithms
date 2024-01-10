# Task = 1(a)
# Topological sort DFS (topological sort must for undirected graph)

inputFile=open('Lab5_input1(a).txt','r')
out=open('Lab5_output1(a).txt','w')
nodes, edges = map(int, inputFile.readline().split())
graph_dict = {}
for i in range(1, nodes + 1):
    graph_dict[i] = []

for i in range(edges):
    u, v = map(int, inputFile.readline().split())
    graph_dict[v].append(u)

col=['White']*(nodes+1)
start=[0]*(nodes+1)
finish=[0]*(nodes+1)

time=0
visited=False
stack = []

def DFS(G,s):
    global time
    global visited
    col[s]='Grey' #processing
    time+=1
    start[s]=time
    for u in G[s]:
        if col[u]=='White': #visit start
            DFS(G,u)
        elif col[u]=='Grey':
            visited=True

    col[s]='Black' #visit Done
    time+=1
    finish[s]=time
    stack.append(s)  # end time er basis e node gulo stack e push hocche. etai track for topological
                    # visit deri te hole, higher finishing time, stack e first e dhukbe. tai high to low finishing time wala node pawar jonno stack ta reverse korte hobe.
def DFS_visit(G):  # (one by one for all node, visit start) or (checking for more than one component and all of them should be visited)
 for v in range(1,nodes+1):
        if col[v]=='White':
            DFS(G,v)
            if visited==True:  # cycle found(adj gulo ghure ashar time e visited adj peye gele)
                out.write('IMPOSSIBLE')
                break

 else:
    stack.reverse()
    while len(stack)!=0:
        sorted=stack.pop()
        out.write(f'{sorted} ')

DFS_visit(graph_dict)
