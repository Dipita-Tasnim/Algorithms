# Task 1 (b)------(Graph representation by Adjacency list)

inputFile = open("Lab4_input1(b).txt", mode = "r")
outputFile = open("Lab4_output1(b).txt", mode = "w")

nodes_edges_tup = tuple(map(int, inputFile.readline().split()))
nodes, edges = nodes_edges_tup  #tuple unpack
# or.. nodes, edges = map(int, inputFile.readline().split())
lst = []
for i in range(edges):
    each_tuple = tuple(map(int, inputFile.readline().split()))
    lst += [each_tuple]
# print(lst)

adj_lst = [""] * (nodes+1)
for i in range(nodes+1):
    adj_lst[i] = []
# print(adj_lst)


for i in lst:
    if i != ():
        m, u, v = i
        if m not in adj_lst:
            adj_lst[m].append((u,v))
        else:
            adj_lst[m] += [(u, v)]

res1 = ""
res2 = ""
for i in range(len(adj_lst)):
    if adj_lst[i] == []:
        # outputFile.write(f"\n{i} : \n")
        res1 += str(i) + ":" + " " + "\n"
        outputFile.write(res1)
        res1 = ""
    else:
        s = " ".join([f"({tup1},{tup2})" for tup1, tup2 in adj_lst[i]]) #1: e duita tup er majhe comma shoranor jonno ei jhamela kora hoyeche. dot join diye ekta lst ke str banano hoy. dot join er aage " " thakle space diye elem gulo alada thakbe str e. aar "," dile comma diye elem gulo str er moddhe separate thakbe.
        # outputFile.write(f"{i} : {s}")
        res2 += str(i) + ":" + " " + str(s) + "\n"
        outputFile.write(res2)
        res2 = ""

inputFile.close()
outputFile.close()