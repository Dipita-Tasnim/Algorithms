# Task 1

# x = inputFile.readline().split()
# y = inputFile.readline().split()
# arr= []
# for i in y:
#   arr.append(int(i))

def merge(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if int(a[i]) < int(b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # result.extend(a[i:])
    # result.extend(b[j:])
    # return result

    if i < len(a):    # Extra elem gulo append hobe. i choto tar mane len porjonto jay nai
      result += a[i:]  # extra elem ache.
    if j < len(b):
      result += b[j:]
    return result
# merge([1,3,5], [2,4,6])

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)

inputFile = open("Lab3_input1.txt", mode = "r")
outputFile = open("Lab3_output1.txt", mode = "w")

n = inputFile.readline()
arr = inputFile.readline().rstrip().split(" ")
sorted = mergeSort(arr)

for i2 in sorted:
    outputFile.write(i2 + " ")
