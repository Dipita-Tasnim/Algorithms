# Task- 2(a)

inputFile = open("input2(a)(Lab2).txt","r")
outputFile = open("output2(a)((Lab2).txt", mode = "w")

p_lst1 = []
lst1 = []
elem1 = int(inputFile.readline())
p_lst1 = inputFile.readline().split()
for i in p_lst1:
    lst1.append(int(i))

p_lst2 = []
lst2 = []
elem2 = int(inputFile.readline())
p_lst2 = inputFile.readline().split()
for i in p_lst2:
    lst2.append(int(i))
# lst1 = [1, 3, 5, 7]
# lst2 = [2, 2, 4, 8]

lst = lst1 + lst2
lst.sort()
# print(lst)

s = ""
for i in lst:
    s += str(i) + " "
outputFile.write(s)

inputFile.close()
outputFile.close()