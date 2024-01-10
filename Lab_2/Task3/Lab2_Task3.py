# Task 3

def maxtask(inputFile):
    n = int(inputFile.readline())
    t1 = []
    t2 = []
    start, end = "", ""
    for i in range(n):
        start, end = inputFile.readline().rstrip().split(" ")
        # print(start)
        # print(end)
        t1 += [(start,end)]
        # print(t1)
    min = 0
    # end time er basis e sort
    for j in range(n - 1):
        min = j
        for k in range(j+1, n):
            if int(t1[k][1]) < int(t1[min][1]):
                min = k
        t1[j], t1[min] = t1[min], t1[j]

    t2 += [t1[0]]  #new_list
    lst = t1[0][1]
    for i in range(1,n):
        if t1[i][0] >= lst:
            t2 += [t1[i]]
            lst = t1[i][1]
    return len(t2), t2

inputFile = open("input3 (Lab2).txt","r")
outputFile = open("output3(Lab2).txt","w")

# outputFile.write("")
a,b = maxtask(inputFile)

outputFile.write(str(a)+"\n")
for i in b:
    outputFile.write(str(i[0])+" "+str(i[1])+"\n")

inputFile.close()
outputFile.close()