# Task 6

def find_kthS(arr, start, end, k):
  if 0 < k <= end - start + 1:   # jehetu 1 based idx bola, tai index 1 theke start
    idx = partition(arr, start, end)
    if idx - start + 1 == k: # pivot tai ans
      return arr[idx]
    elif idx - start + 1 > k:  # pivot er left e ashte hobe  (ekhane idx-start) korar karon pivot er left side er size ta dekhtese kth er cheye kom naki beshi
      return find_kthS(arr, start, idx - 1, k) # left e ashte hobe tai pivot er idx komay dibo
    else:
      return find_kthS(arr, idx + 1, end, k - idx + start - 1)
  return -1


def partition(arr, start, end):
  pivot = arr[end]
  p_idx = start - 1
  for i in range(start, end):
    if arr[i] <= pivot:
      p_idx += 1
      arr[i], arr[p_idx] = arr[p_idx], arr[i]
  arr[p_idx + 1], arr[end] = arr[end], arr[p_idx + 1]
  return int(p_idx + 1)


file = open("Lab3_input6.txt", "r")
output = open("Lab3_output6.txt", "w")
n = int(file.readline().rstrip().split(" ")[0])
arrT = file.readline().rstrip().split(" ")
arr = []
for i1 in range(n):
  arr += [int(arrT[i1])]
q = int(file.readline().rstrip().split(" ")[0])
for i2 in range(q):
  output.write(str(find_kthS(arr, 0, len(arr) - 1, int(file.readline()))) + "\n")