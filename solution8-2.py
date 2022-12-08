grid = list(list(int(i) for i in l.strip()) for l in open("./input8.txt").readlines())
width = len(grid[0])
height = len(grid)
maxScore = 0
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
        rightScore = 0
        for xTest in range(x + 1, width):
            rightScore += 1
            if grid[y][xTest] >= h:
                break
        leftScore = 0
        for xTest in range(x - 1, -1, -1):
            leftScore += 1
            if grid[y][xTest] >= h:
                break
        downScore = 0
        for yTest in range(y + 1, height):
            downScore += 1
            if grid[yTest][x] >= h:
                break
        upScore = 0
        for yTest in range(y - 1, -1, -1):
            upScore += 1
            if grid[yTest][x] >= h:
                break
        score = rightScore * leftScore * upScore * downScore
        if score > maxScore:
            maxScore = score
print(maxScore)