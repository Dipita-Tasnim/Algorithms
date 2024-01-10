# Task 4 (in process)

def find_val(arr):
  max1 = max2 = -9999999
  idx1 = idx2 = -1
  for i1 in range(1, len(arr)):
    if abs(arr[i1]) >= max1:
      idx1 = i1
      max1 = abs(arr[i1])
  for i2 in range(0, idx1):
    if abs(arr[i2]) > max2:
      idx2 = i2
      max2 = arr[i2]
  return arr[idx2] + (arr[idx1] ** 2)


file = open("Lab3_input4.txt", "r")
output = open("Lab3_output4.txt", "w")
for i in range(3):
  output.write(file.readline())
  n = file.readline()
  arrT = file.readline().rstrip().split(" ")
  arr = []
  for i2 in range(int(n)):
    arr += [int(arrT[i2])]
  output.write(str(find_val(arr)) + "\n")