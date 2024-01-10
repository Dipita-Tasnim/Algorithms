# Task 4

inputFile= open("input4.txt", "r")
outputFile= open("output4.txt", "w")
input_list= inputFile.readlines()
name = []
time = []
location = []

for i in range(int(input_list[0])):
  name.append(input_list[i+1].split(" ")[0])
  time.append(input_list[i+1].split(" ")[6])
  location.append(input_list[i+1].split(" ")[4])                                         


for i in range(len(name) - 1):
  for j in range(len(name) - i - 1):
    if name[j] > name[j + 1]:
        temp_nem = name[j]
        temp_tim = time[j]
        temp_loc = location[j]
        name[j] = name[j+1]
        time[j] = time[j+1]
        location[j] = location[j+1]
        name[j+1] = temp_nem
        time[j+1] = temp_tim
        location[j+1] = temp_loc

for j in range(len(name)):
  for i in range(len(name)-1):
    if name[i] == name[i+1]:
      if time[i] < time[i+1]:
          time[i], time[i+1] = time[i+1], time[i]
          location[i], location[i+1] = location[i+1], location[i]

for i in range(len(name)):
  outputFile.write(f"{name[i]} will departure for {location[i]} at {time[i]}\n")

inputFile.close()
outputFile.close()





