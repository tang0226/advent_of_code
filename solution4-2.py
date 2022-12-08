lines = open("./input4.txt").readlines()
total = 0
for l in lines:
	line = l.strip()
	roomPairs = line.split(",")
	range1 = list(int(i) for i in roomPairs[0].split("-"))
	range2 = list(int(i) for i in roomPairs[1].split("-"))
	if (range1[1] >= range2[0] and range1[0] <= range2[1]) or (range2[1] >= range1[0] and range2[0] <= range1[1]):
		total += 1
print(total)