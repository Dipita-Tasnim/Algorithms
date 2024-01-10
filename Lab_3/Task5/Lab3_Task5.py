# Task 5

def quicksort(arr, start, end):
  if int(start) < int(end): #base case(start,end ta i,j er motot duita pointer)
    part_pos = partition(arr, start, end)
    # pivot jayga moto boshe gese.
    quicksort(arr, start, part_pos - 1) #ebar pivot er aager part sort
    quicksort(arr, part_pos + 1, end)  # pivot er porer part sort


def partition(arr, start, end): #pivot ke jayga moto boshano--
  pivot = int(arr[int(end)])   # dhore nibo last elem
  p_idx = int(start) - 1
  for i in range(int(start), int(end)):
    if int(arr[i]) <= pivot:
      p_idx += 1
      arr[i], arr[p_idx] = arr[p_idx], arr[i]
  arr[p_idx + 1], arr[end] = arr[end], arr[p_idx + 1] #last e thaka pivot ke swap korchi.
  return int(p_idx + 1)


file = open("Lab3_input5.txt", "r")
output = open("Lab3_output5.txt", "w")


n = file.readline()
arr = file.readline().rstrip().split(" ")
quicksort(arr, 0, len(arr) - 1)
for i2 in arr:
  output.write(i2 + " ")
