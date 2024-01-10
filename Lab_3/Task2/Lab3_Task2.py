# Task 2

inputFile = open("Lab3_input2.txt", mode = "r")
outputFile = open("Lab3_output2.txt", mode = "w")
# x = inputFile.readline().split()
# y = inputFile.readline().split()
# arr= []
# for i in y:
#   arr.append(int(i))

def find_max(a1, a2):
  if int(a1[0]) > int(a2[0]):
    return a1
  else:
    return a2

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])  # write the parameter
        a2 = mergeSort(arr[mid:])  # write the parameter
        return find_max(a1, a2)

n = inputFile.readline()
arr = inputFile.readline().rstrip().split(" ")
outputFile.write(str(mergeSort(arr)[0]) + "\n")

# The complexity of this code is O(nlogn).