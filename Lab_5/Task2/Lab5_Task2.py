# Task 2
#Topological sort with Lexicographical order

from queue import Queue
q = Queue()
inputFile = open('Lab5_input1(b).txt', 'r')
out = open('Lab5_output(b).txt', 'w')

nodes, edges = map(int, inputFile.readline().split())
graph_dict = {}
indegree = [0] * (nodes + 1)

for i in range(1, nodes + 1):
    graph_dict[i] = []

for i in range(edges):
    u, v = map(int, inputFile.readline().split())
    graph_dict[u].append(v)
    indegree[v] += 1

path = []
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
for i in range(1, int(nodes) + 1):
    if not visited:
        Cycle_Check(i)

# Modified BFS function to output lexicographically smallest sequence
def BFS(G):
    result = []
    for i in range(1, nodes + 1):
        if indegree[i] == 0:
            q.put(i)
    while not q.empty():
        u = q.get()
        result.append(u)
        for v in sorted(G[u]):  # Sort the neighbors lexicographically
            indegree[v] -= 1
            if indegree[v] == 0:
                q.put(v)
    return result

if visited:
    out.write('IMPOSSIBLE')
else:
    result_sequence = BFS(graph_dict)
    for i in result_sequence:
        out.write(f'{i} ')
