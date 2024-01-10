# Task 1 (a)

fileInput = open("input1a.txt","r")
outputFile = open("output1a.txt","w")

x = int(fileInput.readline())

for i in range(x):
  y = int(fileInput.readline())
  if y % 2 == 0:
    outputFile.write(f"{y} is an even number.\n")
  else:
    outputFile.write(f"{y} is an odd number.\n")

outputFile.close()
fileInput.close()