# Task 2

import math

def bfs(queue, visited, adjL, rel):
  list1 = []
  while len(queue) != 0:
    list1 = adjL[queue[0]]
    if len(list1) != 0:
      for i3 in list1:
        if rel[i3[0]] > i3[1] + rel[queue[0]]:
          rel[i3[0]] = i3[1] + rel[queue[0]]
        if i3[0] not in visited and i3[0] not in queue:
          queue += [i3[0]]
    visited += [queue[0]]
    queue.pop(0)


def adjList(file, n, m):
  adjL = []
  u = v = w = 0
  for i1 in range(n + 1):
    adjL += [[]*(n + 1)]
  for i2 in range(m):
    u, v, w = map(int, file.readline().rstrip().split(" "))
    adjL[u] += [(v, w)]
  return adjL


def meetup(file, output):
  n, m = map(int, file.readline().rstrip().split(" "))
  adjL = adjList(file, n, m)
  relaxA = [math.inf] * (n + 1)
  relaxB = [math.inf] * (n + 1)
  visitedA = []
  visitedB = []

  s, t = map(int, file.readline().rstrip().split(" "))
  queueA = [s]
  relaxA[s] = 0
  queueB = [t]
  relaxB[t] = 0

  bfs(queueA, visitedA, adjL, relaxA)
  for i4 in range(1, n + 1):
    if relaxA[i4] == math.inf:
      relaxA[i4] = -1

  bfs(queueB, visitedB, adjL, relaxB)
  for i5 in range(1, n + 1):
    if relaxB[i5] == math.inf:
      relaxB[i5] = -1

  flag = False
  common_spots = [math.inf] * (n + 1)
  for i6 in range(1, n + 1):
    if relaxA[i6] != -1 and relaxB[i6] != -1:
      common_spots[i6] = abs(relaxA[i6] - relaxB[i6])
      flag = True

  if flag == False:
    output.write("Impossible")
  else:
    time = min(common_spots)
    idx = common_spots.index(time)
    if relaxA[idx] > relaxB[idx]:
      output.write(f"Time {relaxA[idx]}\nNode {idx}")
    else:
      output.write(f"Time {relaxB[idx]}\nNode {idx}")


file1 = open("Lab6_input2.txt", "r")
output1 = open("Lab6_output2.txt", "w")
meetup(file1, output1)
