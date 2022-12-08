data = ""
with open("./1-input.txt") as fp:
    line = fp.readline()
    while(line):
        if line == "\n":
            data += "\n"
        else:
            data += line.strip() + " "
        line = fp.readline()
print(max(sum(int(i) for i in j.split(" ") if i != "") for j in data.split("\n")))
