lines = open("./input6.txt").readlines()


word = lines[0]
#word = "bvwbjplbgvbhsrlpgdmjqwftvncz"
for i in range(14, len(word)):
	c = list(j for j in word[i - 14 : i])
	if len(set(c)) == len(c):
		print(i)
		break