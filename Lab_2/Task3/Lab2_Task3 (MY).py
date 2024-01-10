inputFile = open("input3 (Lab2).txt", mode = "r")
outputFile = open("output3(Lab2).txt", mode = "w")

x = int(inputFile.readline())
sub_lst = []
lst = []
for i in range(x):
  sublist = inputFile.readline().split()
  lst.append(sublist)
print(lst)

# Sorting according to the second part of each sublist.
for i in range(len(lst)):
    min_index = i
    for j in range(i + 1, len(lst)):
        if int(lst[j][1]) < int(lst[min_index][1]):
            min_index = j
    (lst[i], lst[min_index]) = (lst[min_index], lst[i])
print(lst)


i = 0
j = 1
count = 1
result = [lst[0]]

while i < (x-1) and j <= x:
    if int(lst[i][1]) <= int(lst[j][0]):
        count += 1
        result.append(lst[j])
        if abs(i-j) == 2:
            i += 2
        elif abs(i-j) == 1:
            i += 1
        j += 1
    else:
        j += 1

outputFile.write(str(count)+ "\n")

string = ""
for i in result:
    string += ' '.join(i) + "\n"
string = string.rstrip("\n")
outputFile.write(string)
