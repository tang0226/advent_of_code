lines = list(l.strip() for l in open("./input3.txt").readlines())
alpha = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0
for n in range(0, len(lines), 3):
    done = False
    for c1 in lines[n]:
        if done:
            break
        for c2 in lines[n + 1]:
            if done:
                break
            for c3 in lines[n + 2]:
                if c1 == c2 == c3:
                    total += alpha.index(c1)
                    done = True
                    break
print(total)