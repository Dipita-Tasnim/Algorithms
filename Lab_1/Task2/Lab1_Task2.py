# Task 2

inputFile = open("input2.txt",mode = "r")
outputFile = open("output2.txt",mode = "w")
num = inputFile.readline()
string = inputFile.readline().split()
arr = []

for i in string:
    arr.append(int(i))

def isSorted(arr):
    for i in range (len(arr)-1):
      if arr[i]>arr[i+1]:
        return False
    return True


def bubbleSort(arr):
    flag = isSorted(arr)
    if flag == True:
      return

    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubbleSort(arr)

s = ""
for i in arr:
    s += str(i) + " "
outputFile.write(s)

inputFile.close()
outputFile.close()

# How I achieved theta(n) for the best case scenario-

# I am checking that if all the elements of array have already sorted or not. therefore each of the elements of the array must be smaller than the next one(ascending).
# So, if there any element that is greater than the next one, then it is definitely not sorted and it should return False and bubbleSort() function will work
# for that array. Otherwise for the best case scenario(already sorted array), after checking all the elements, we get True and immediately return.
# So, for this sorted array, no need to execute the bubbleSort() function. Thus I achieved theta(n) for the best case scenario.