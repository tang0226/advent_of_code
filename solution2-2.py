games = list(line.split(" ") for line in open("./2-input.txt").read().split("\n"))
total = 0
val = {
	"A": 1,
	"B": 2,
	"C": 3
}
win = {
	"A": "B",
	"B": "C",
	"C": "A"
}
lose = {
	"A": "C",
	"B": "A",
	"C": "B"
}
for game in games:
	opp = game[0]
	you = game[1]
	if you == "X":
		total += val[lose[opp]]
	elif you == "Y":
		total += val[opp] + 3
	else:
		total += val[win[opp]] + 6
print(total)