# Task 3

inputFile = open('input3.txt', 'r')
outputFile = open('output3.txt','w')

num= int(inputFile.readline())

id  = inputFile.readline().split()
arr_id = []
for i in id:
    arr_id.append(int(i))

marks = inputFile.readline().split()
arr_marks = []
for i in marks:
    arr_marks.append(int(i))

def selection_sort(arr_marks,arr_id):
  for i in range(len(arr_marks)):
    max_idx = i
    for j in range(i+1,len(arr_marks)):
      if arr_marks[j] >= arr_marks[max_idx] :
        if arr_marks[j] == arr_marks[max_idx] and arr_id[j] > arr_id[max_idx]:
         continue
        max_idx = j
    temp = arr_marks[max_idx]
    T = arr_id[max_idx]
    arr_marks[max_idx] = arr_marks[i]
    arr_id[max_idx] = arr_id[i]
    arr_marks[i] = temp
    arr_id[i] = T

selection_sort(arr_marks,arr_id)

for i in range(num):
  if i!= num-1:
      outputFile.write(f'Id:{arr_id[i]} Mark:{arr_marks[i]}\n')
  else:
      outputFile.write(f'Id:{arr_id[i]} Mark:{arr_marks[i]}')

inputFile.close()
outputFile.close()