data = ""
with open("./1-input.txt") as fp:
    line = fp.readline()
    while(line):
        if line == "\n":
            data += "\n"
        else:
            data += line.strip() + " "
        line = fp.readline()
x = list(sum(int(i) for i in j.split(" ") if i != "") for j in data.split("\n"))
x.sort()
print(sum(x[-3:]))
