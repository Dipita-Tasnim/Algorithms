 #Task 5------(Finding Shortest Path for unweighted graph)---follow the second method

inputFile = open("Lab4_input5.txt", mode="r")
outputFile = open("Lab4_output5.txt", mode="w")


# Read input + adj_list(graph_dict) create
nodes, edges, D = map(int, inputFile.readline().split())  # python e jekhane iterate kora jay, oitai evabe unpack kora jay(not just tuple).
graph_dict = {}
for i in range(1, nodes + 1):
    graph_dict[i] = []

for i in range(edges):
    u, v = map(int, inputFile.readline().split())
    graph_dict[u].append(v)
    graph_dict[v].append(u)


def dijkstra(graph, start, end):
    n = len(graph)
    distances = [float('inf')] * (n + 1)  # initially distance infinity dhore nicchi(unreachable)
    visited = [False] * (n + 1)
    prev = [-1] * (n + 1)
    distances[start] = 0

    for _ in range(n):
        # unvisited node with the minimum distance ber korchi
        min_distance = float('inf')
        current = -1

        for node in range(1, n + 1):
            if visited[node] == False and distances[node] < min_distance:
                min_distance = distances[node]
                current = node

        if current == -1:
            break

        visited[current] = True

        for adj_i in graph[current]:
            if distances[current] + 1 < distances[adj_i]:  #formula--ekhane weight=1 dhora hoyeche
                distances[adj_i] = distances[current] + 1
                prev[adj_i] = current

    path = []
    node = end

    while node != -1:
        path.append(node)
        node = prev[node]

    return distances[end], path[::-1]

time, path = dijkstra(graph_dict, 1, D)

outputFile.write(f"Time: {time}\n")
outputFile.write(f"Shortest Path: {' '.join(map(str, path))}")

inputFile.close()
outputFile.close()

# using bfs
 # from collections import deque
 #
 #
 # def bfs_shortest_path(graph, start):
 #     # Create a queue and add the starting vertex to it
 #     queue = deque([start])
 #
 #     # Create an array to keep track of the distances from the starting vertex to all other vertices
 #     distances = [float('inf')] * len(graph)
 #     distances[start] = 0
 #
 #     # Create a set to keep track of visited vertices
 #     visited = set()
 #
 #     # Perform BFS
 #     while queue:
 #         # Dequeue the next vertex
 #         vertex = queue.popleft()
 #         visited.add(vertex)
 #
 #         # Update the distances of neighbors
 #         for neighbor in graph[vertex]:
 #             if neighbor not in visited:
 #                 distances[neighbor] = distances[vertex] + 1
 #                 queue.append(neighbor)
 #
 #     return distances
 #
 #
 # # Example graph: unweighted, directed graph with 5 vertices
 # # Vertices are represented by integers 0 through 4
 # # Edges: (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4)
 #
 # graph = [[1, 2], [2, 3], [3], [4], []]
 #
 # start_vertex = 0
 # distances = bfs_shortest_path(graph, start_vertex)
 #
 # print(distances)  # Output: [0, 1, 1, 2, 3]