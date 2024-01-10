# task 1(a)

inputFile = open("input1(a)Lab2.txt", mode = "r")
outputFile = open("output1(a)Lab2.txt", mode = "w")

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
for i in range(len(a_arr)):
  for j in range(len(a_arr)):
    if a_arr[i] + a_arr[j] == target:
      flag = True
      break
      # outputFile.write(f"{j+1} {i+1}")
    else:
      # outputFile.write(f"IMPOSSIBLE")
      flag = False

if flag == True:
  outputFile.write(f"{j + 1} {i + 1}")
else:
  outputFile.write(f"IMPOSSIBLE")

inputFile.close()
outputFile.close()

