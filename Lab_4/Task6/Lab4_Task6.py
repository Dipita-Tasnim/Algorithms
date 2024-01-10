# Task 6

inputFile = open("Lab4_input6.txt", mode="r")
outputFile = open("Lab4_output6.txt", mode="w")

row, col = map(int, inputFile.readline().split())
grid = [inputFile.readline().strip() for i in range(row)]


def flood_fill(grid, visited, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '#' or visited[row][col]:
        return 0

    visited[row][col] = True
    collected_D = 0   #per iteration e 0 hoy but ma_D update hote thake. max_D initially 0 thake.

    if grid[row][col] == 'D':
        collected_D = 1

    collected_D += flood_fill(grid, visited, row + 1, col)
    collected_D += flood_fill(grid, visited, row - 1, col)
    collected_D += flood_fill(grid, visited, row, col + 1)
    collected_D += flood_fill(grid, visited, row, col - 1)

    return collected_D   #for per starting point(0,1)/or(0,2)...er l,r,up,down.

def max_diamonds(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    max_D = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.' and not visited[i][j]:
                collected_D = flood_fill(grid, visited, i, j)
                max_D = max(max_D, collected_D)

    return max_D

result = max_diamonds(grid)

outputFile.write(str(result))

inputFile.close()
outputFile.close()