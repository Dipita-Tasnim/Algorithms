# Task 3-----(DFS Traversal)

inputFile = open("Lab4_input3.txt", mode="r")
outputFile = open("Lab4_output3.txt", mode="w")


# Read input + adj_list(graph_dict) create
nodes, edges = map(int, inputFile.readline().split())  # python e jekhane iterate kora jay, oitai evabe unpack kora jay(not just tuple).
graph_dict = {}
for i in range(1, nodes + 1):
    graph_dict[i] = []

for i in range(edges):
    u, v = map(int, inputFile.readline().split())
    graph_dict[u].append(v)
    graph_dict[v].append(u)

# graph_dict-
# {1: [3, 4], 2: [3], 3: [1, 2], 4: [1]}

def dfs(graph, start):
    visited = [False] * (len(graph) + 1)
    path = []

    def dfs_recursive(current_node):
        path.append(current_node)
        visited[current_node] = True

        for adj_i in graph[current_node]:   # adj_i true hoye jay(unvisited adj_i na pele and oi node er kono adj_i baki na thakle recursion er rule wise back track hobe auto. mane tar aager node e ferot jeye shei node er unvisited adj_i khujbe (karon aager node er shob unvisited adj check kora hoy nai, baki chilo orthat check korar aagei recursive case e chole jacchilo..tai ebar sheikhane ferot jabe aar check korbe.) , erporeo na pele oikhanei code shesh.
            if visited[adj_i] == False:
                dfs_recursive(adj_i) # recursive call

    dfs_recursive(start) #func. call
    return path

result_path = dfs(graph_dict, 1)
outputFile.write(" ".join(map(str, result_path)))

inputFile.close()
outputFile.close()