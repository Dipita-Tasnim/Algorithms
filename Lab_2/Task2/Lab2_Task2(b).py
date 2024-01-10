# Task 2 (b)--O(n)

inputFile = open("input2(b)(Lab2).txt","r")
outputFile = open("output2(b)(Lab2).txt", mode = "w")

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
lst = []
i = 0
j = 0

# merge funtion
while i < len(lst1) and j < len(lst2):
    if lst1[i] < lst2[j]:
        lst.append(lst1[i])
        i += 1
    elif lst2[j] < lst1[i]:
        lst.append(lst2[j])
        j += 1
    elif lst1[i] == lst2[j]:
        lst.append(lst1[i])
        lst.append(lst2[j])
        i += 1
        j += 1

for i in lst1:
    if i not in lst:
        lst.append(i)

for i in lst2:
    if i not in lst:
        lst.append(i)

s = ""
for i in lst:
    s += str(i) + " "
outputFile.write(s)

inputFile.close()
outputFile.close()