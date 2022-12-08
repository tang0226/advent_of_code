lines = open("./input6.txt").readlines()


word = lines[0]
#word = "bvwbjplbgvbhsrlpgdmjqwftvncz"
for i in range(4, len(word)):
	c = list(j for j in word[i - 4 : i])
	if len(set(c)) == len(c):
		print(i)
		break