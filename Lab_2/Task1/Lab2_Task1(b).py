# Task 1(b)

inputFile = open("input1(b)Lab2.txt","r")#.readlines()
outputFile = open("output1(b)Lab2.txt","w")

# a = inputFile[0].split("\n")
# var = inputFile[0].split(' ')
# var1 = inputFile[1].split(' ')

x = inputFile.readline().split()
x_arr= []
for i in x:
  x_arr.append(int(i))
target = x_arr[1]

a = inputFile.readline().split()
a_arr= []
for i in a:
  a_arr.append(int(i))

flag = False
i = 0
j = len(a_arr)-1

while (i < j):
 if int(a_arr[i]) + int(a_arr[j]) == target:
  flag = True
  outputFile.write(f"{i+1} {j+1}")
  break

 elif int(a_arr[i]) + int(a_arr[j]) < target:
  i = i + 1

 elif int(a_arr[i]) + int(a_arr[j]) > target:
  j = j - 1

if flag == False :
    outputFile.write(f"IMPOSSIBLE")
