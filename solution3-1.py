lines = list(l.strip() for l in open("./input3.txt").readlines())
alpha = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0
for sack in lines:
    i = len(sack) // 2

    s1 = sack[ : i]
    s2 = sack[i : ]
    done = False
    for c1 in s1:
        if done:
            break
        for c2 in s2:
            if c1 == c2:
                total += alpha.index(c1)
                done = True
                break
print(total)