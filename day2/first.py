print("Advent of code, day 2")
f = open("input")
lines = f.readlines()
f.close()
h = 0
depth = 0
for line in lines:
    cmd = line.split()
    if cmd[0] == "forward":
        h += int(cmd[1])
    if cmd[0] == "up":
        depth -= int(cmd[1])
    if cmd[0] == "down":
        depth += int(cmd[1])

print(h * depth)