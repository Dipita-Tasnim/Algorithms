# Task 3

def find(rep, par):
  if par[rep] == rep:
    return rep
  return find(par[rep], par)


def friend_circle(file, output):

  integers = file.readline().rstrip().split(" ")
  n, k = int(integers[0]), int(integers[1])

  parent = [None] * (n + 1)
  count = 0

  for i1 in range(n + 1):
    parent[i1] = i1
  for i2 in range(k):
    integers = file.readline().rstrip().split(" ")
    a, b = int(integers[0]), int(integers[1])
    parA = find(a, parent)
    parB = find(b, parent)
    if parA != parB:
      parent[parB] = parA
    count = 0
    for i3 in range(n):
      if find(parent[i3], parent) == parA:
        count += 1
    output.write(str(count) + "\n")


file1 = open("Lab6_input3.txt", "r")
output1 = open("Lab6_output3.txt", "w")
friend_circle(file1, output1)
