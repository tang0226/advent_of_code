games = list(line.split(" ") for line in open("./2-input.txt").read().split("\n"))
total = 0
lose = {
	"A": "Y",
	"B": "Z",
	"C": "X"
}
tie = {
	"A": "X",
	"B": "Y",
	"C": "Z"
}
val = {
	"X": 1,
	"Y": 2,
	"Z": 3
}
for game in games:
	total += val[game[1]]
	if lose[game[0]] == game[1]:
		total += 6
	elif tie[game[0]] == game[1]:
		total += 3
	else:
		total += 0
print(total)