# Task 2

inputFile = open("Lab4_input2.txt", mode="r")
outputFile = open("Lab4_output2.txt", mode="w")


# Read input + adj_list(graph_dict) create
nodes, edges = map(int, inputFile.readline().split())  # python e jekhane iterate kora jay, oitai evabe unpack kora jay(not just tuple).
graph_dict = {}
for i in range(1, nodes + 1):  #starting from 1 (according to Q.)
    graph_dict[i] = []

for i in range(edges):
    u, v = map(int, inputFile.readline().split())
    graph_dict[u].append(v)
    graph_dict[v].append(u)

# graph_dict-
# {1: [3, 4], 2: [3], 3: [1, 2], 4: [1]}

# Queue ke normal list hishebe dhore code ta korleo hobe. Ekhane dequeue() func. use kore kora hoise.
from collections import deque

def bfs(graph, start):
    visited = [False] * (len(graph) + 1)  #1 no.idx and last idx (majher gulo shoho) ta lagbe(0 no. idx baad). Tai (len+1) kora hoyeche.
    queue = deque([start])
    path = []

    while queue != deque([]):
        current_node = queue.popleft() # 1 deleted
        # list diye korle pop[0] dite hoto.
        path.append(current_node)   # current_node = 1
        visited[current_node] = True
        # print(visited)
        for adj_i in graph[current_node]:
            if visited[adj_i] == False:
                queue.append(adj_i)
                visited[adj_i] = True

    return path

result_path = bfs(graph_dict, 1)
outputFile.write(" ".join(map(str, result_path)))

inputFile.close()
outputFile.close()








