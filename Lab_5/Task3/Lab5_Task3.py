# Task 3
# Finiding Strongly Connected Component (directed graph e each node must reach to each node)

inputFile = open('Lab5_input3.txt', 'r')
out = open('Lab5_output3.txt', 'w')

nodes, edges = map(int, inputFile.readline().split())
graph_dict = {}
Transpose_graph = {}
for i in range(1, nodes + 1):
    graph_dict[i] = []
    Transpose_graph[i] = []
for i in range(edges):
    u, v = map(int, inputFile.readline().split())
    graph_dict[u].append(v)
    Transpose_graph[v].append(u) # normal graph and transpose graph eksathe create

col = ['White']*(nodes+1)
start = [0] * (nodes+1)
finish = [0] * (nodes+1)
indegree = [0] * (nodes + 1)
time = 0

stack=[]
path=[]
store=[]

def DFS_visit(G):
    for v in range(1,nodes+1):
        if col[v] == 'White':
            DFS(G, v)

def DFS(graph_dict, s):
    global time
    col[s] = 'Grey'
    time += 1
    start[s] = time
    for u in graph_dict[s]:
        if col[u] == 'White':
            DFS(graph_dict, u)
    col[s] = 'Black'
    time += 1
    finish[s] = time
    stack.append(s)

DFS_visit(graph_dict)

col=['White'] * (nodes+1)

def newDFS(Transpose_graph, u):
    col[u] = 'Grey'  # stack theke pop korar serial e ekta ekta node traverse hobe
    path.append(u)  # path e ekekta componenet er shob elem ashbe resest hoye hoye alada vabe list hishebe
    for v in Transpose_graph[u]:
        if col[v] == 'White':
            newDFS(Transpose_graph, v)
    col[u] = 'Black'

for u in range(1,nodes+1):
    if col[u] == 'White':
        newDFS(Transpose_graph, u)
        path.sort()  # not necessary
        store.append(path)  # store e path er ekekta component er list of element append hobe
        path = []

for t in store: # t te ekek ta list jabe separate component set gulor
    out.write(f"{' '.join(map(str, t))} \n")
