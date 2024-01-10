# Task 4-----(Cycle Finding)

inputFile = open("Lab4_input4.txt", mode="r")
outputFile = open("Lab4_output4.txt", mode="w")


# Read input + adj_list(graph_dict) create
nodes, edges = map(int, inputFile.readline().split())  # python e jekhane iterate kora jay, oitai evabe unpack kora jay(not just tuple).
graph_dict = {}
for i in range(1, nodes + 1):
    graph_dict[i] = []

for i in range(edges):
    u, v = map(int, inputFile.readline().split())
    graph_dict[u].append(v)
    # graph_dict[v].append(u) --Eta hobe na karon eta undirected na.


def has_cycle(graph, node, visited, call_stack): # ekhane ekta kore current node ashtese aar check hocche cycle ache kina.

    visited[node] = True #for preventing revisit
    call_stack[node] = True #for identifying cycle

    for neighbor in graph[node]:
        if visited[neighbor] == False:
            has_cycle(graph, neighbor, visited, call_stack)
            # return True
        elif call_stack[neighbor] == True:
            return True

    call_stack[node] = False
    return False

def contains_cycle(graph, n): # proti ta node ke calculation e anbo and has cycle e pathay dicchi check korar jonno cycle ache kina

    visited = [False] * (n + 1)
    call_stack = [False] * (n + 1)

    for node in range(1, n + 1):
        if visited[node] == False:
            has_cycle(graph, node, visited, call_stack)
    #         return True
    #
    # return False

if contains_cycle(graph_dict, nodes): #func. theke true return hoye ashle
    outputFile.write("YES")
else:
    outputFile.write("NO")

inputFile.close()
outputFile.close()