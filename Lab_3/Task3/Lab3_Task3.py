# Task 3

def helper(arr, compV):
  if len(arr) < 1:
    return []
  if len(arr) == 1 or arr[0] < compV: #checking part_compV te boro val thakbe.
      return arr
  else:
      mid = len(arr)//2
      a1 = helper(arr[:mid], compV)
      a2 = helper(arr[mid:], compV)
      return a1 + a2


def count_smaller(arr, compV):
  count = 0
  for i in range(len(arr)):
    l1 = helper(arr[i + 1: ], arr[i])
    count += len(l1)
  return count


file = open("Lab3_input3.txt", "r")
output = open("Lab3_output3.txt", "w")

a = file.readline()
arrT = file.readline().rstrip().split(" ")
arr = []
for i1 in range(int(a)):
  arr += [int(arrT[i1])]
output.write(str(count_smaller(arr, 0)))