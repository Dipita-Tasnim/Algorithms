# Task 1 (a)------(Graph representation by Adjacency Matrix)

inputFile = open("Lab4_input1(a).txt", mode = "r")
outputFile = open("Lab4_output1(a).txt", mode = "w")

nodes_edges_tup = tuple(map(int, inputFile.readline().split()))
nodes, edges = nodes_edges_tup  #tuple unpack

lst = []
for i in range(nodes+1):
  each_tuple = tuple(map(int, inputFile.readline().split()))
  lst += [each_tuple]
# print(lst)


def create_adjacency_matrix(nodes):
  # 1D
  adj_matrix = [0] * (nodes + 1)  #Q. e deya total nodes 1 theke count hoyeche. but arr create er time e 0 theke count hoy tai +1 kora hoyeche.

  # 2D
  for i in range(len(adj_matrix)):
      adj_matrix[i] = [0] * (nodes + 1)
  # print(adj_matrix)
  for i in lst:
    row_pos, col_pos, weight = i  #tuple unpack
    adj_matrix[row_pos][col_pos] = weight
  return adj_matrix


def print_adjacency_matrix(matrix, filename):
  for row in matrix:
    row_str = " ".join(map(str, row)) + "\n"
    outputFile.write(row_str)

result = create_adjacency_matrix(nodes)
print_adjacency_matrix(result, 'output.txt')

inputFile.close()
outputFile.close()