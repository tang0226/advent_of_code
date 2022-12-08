lines = list(l for l in open("./input5.txt").readlines())
for l in range(len(lines)):
	if lines[l][-1] == "\n":
		lines[l] = lines[l][ : -1]
rows = []
numColumns = 0
for l in lines:
	if l[ : 2] == " 1":
		numColumns = int(l[-2])
		break
	row = []
	for i in range(0, len(l), 4):
		if l[i] == "[":
			row.append(l[i + 1])
		else:
			row.append(0)
	rows.append(row)
columns = list(list(rows[y][x] for y in range(len(rows) - 1, -1, -1) if rows[y][x] != 0) for x in range(numColumns))
for r in rows:
	print(r)
print(columns)
for l in lines[len(rows) + 2 : ]:
	i1 = l.index(" from ")
	i2 = l.index(" to ")
	amount = int(l[5 : i1])
	From = int(l[i1 + 6 : i2]) - 1
	to = int(l[i2 + 4 : ]) - 1
	add = columns[From][-amount : ]
	columns[From] = columns[From][ : -amount]
	columns[to] += add
	print(l, columns, From, to, amount)
ans = ""
for i in columns:
	ans += i[-1]
print(ans)