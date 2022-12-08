grid = list(list(int(i) for i in l.strip()) for l in open("./input8.txt").readlines())
width = len(grid[0])
height = len(grid)
total = 2 * (width + height) - 4
for i in grid:
    print(i)
def allTrue(arr):
    for i in arr:
        if not i:
            return False
    return True
for x in range(1, width - 1):
    for y in range(1, height - 1):
        h = grid[y][x]
        visible = False
        t1 = list(grid[y][xTest] < h for xTest in range(x + 1, width))
        t2 = list(grid[y][xTest] < h for xTest in range(x - 1, -1, -1))
        t3 = list(grid[yTest][x] < h for yTest in range(y + 1, height))
        t4 = list(grid[yTest][x] < h for yTest in range(y - 1, -1, -1))
        
        if allTrue(t1) or allTrue(t2) or allTrue(t3) or allTrue(t4):
            print(x, y)
            total += 1
print(total)