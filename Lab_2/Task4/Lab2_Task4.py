# Task 4

inputFile = open('input4(Lab2).txt','r')
outputFile = open('output4(Lab2).txt','w')

n, m = inputFile.readline().strip().split(' ')
n,m = int(n),int(m)
G = []

for a in range(n):
    s, e = inputFile.readline().strip().split(' ')
    s,e = int(s),int(e)
    G.append((s, e))

G.sort(key = lambda x:x[1])  #sort korlam basis of end time

task = [0] * m
count = 0

def assinged_activities(arr, m):
    global count
    for i in range(len(arr)):
        start, end = G[i]
        assign = float('inf')  # assign e start-time, end-time er difference thakbe kono ekjoner
        a_idx = -1
        for j in range(m):
            if task[j] <= start:  #korte parbe?
                if assign > start - task[j]:   #Aage korte parbe? #dujoner moddhe kake deya uchit(jar difference kom)
                    assign = start - task[j]
                    a_idx = j

        if assign != float('inf'):
            task[a_idx] = end
            count += 1

assinged_activities(G,m)
outputFile.write(f'{count}')

inputFile.close()
outputFile.close()

