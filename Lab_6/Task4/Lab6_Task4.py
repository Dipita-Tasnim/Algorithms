# Task 4

def find(rep, par):
  if par[rep] == rep:
    return rep
  return find(par[rep], par)


def lowest_cost(file, output):
  integers = file.readline().rstrip().split(" ")
  n, m = int(integers[0]), int(integers[1])

  parent = [None] * (n + 1)
  for i1 in range(n + 1):
    parent[i1] = i1

  cost = u = v = w = 0
  list1 = []

  for i2 in range(m):
    integers = file.readline().rstrip().split(" ")
    u, v, w = int(integers[0]), int(integers[1]), int(integers[2])
    list1.append((w, u, v))
  list1.sort()

  for i3 in list1:
    parA = find(i3[1], parent)
    parB = find(i3[2], parent)
    if parA != parB:
      parent[parA] = parB
      cost += i3[0]
  output.write(str(cost))


file1 = open("Lab6_input4.txt", "r")
output1 = open("Lab6_output4.txt", "w")
lowest_cost(file1, output1)
