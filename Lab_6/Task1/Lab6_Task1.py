# Task 1

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


def dijkstra(file, output):
  n, m = map(int, file.readline().rstrip().split(" "))
  adjL = adjList(file, n, m)
  relax = [math.inf] * (n + 1)
  visited = []
  s = int(file.readline())
  queue = [s]
  relax[s] = 0
  bfs(queue, visited, adjL, relax)
  for i4 in range(1, n + 1):
    if relax[i4] == math.inf:
      output.write("-1 ")
    else:
      output.write(str(relax[i4]) + " ")


file1 = open("Lab6_input1.txt", "r")
output1 = open("Lab6_output1.txt", "w")
dijkstra(file1, output1)
