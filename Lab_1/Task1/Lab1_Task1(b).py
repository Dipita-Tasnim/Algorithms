# Task 1 (b)

inputFile = open("input1b.txt", mode = "r")
outputFile = open("output1b.txt", mode = "w")

x = int(inputFile.readline())

for i in range(x):
  y = inputFile.readline().split()
  one = y[0]
  two = y[1]
  three = y[2]
  four = y[3]

  if three == "+":
    sum = int(two) + int(four)
    outputFile.write(f"The result of {two} {three} {four} is {sum}\n")
  elif three == "-":
    sub = int(two) - int(four)
    outputFile.write(f"The result of {two} {three} {four} is {sub}\n")
  elif three == "*":
    mul = int(two) * int(four)
    outputFile.write(f"The result of {two} {three} {four} is {mul}\n")
  elif three == "/":
    div = int(two) / int(four)
    outputFile.write(f"The result of {two} {three} {four} is {div}\n")

inputFile.close()
outputFile.close()
