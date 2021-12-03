print("Advent of code, day 2")
f = open("input")
lines = f.readlines()
f.close()
h = 0
depth = 0
aim = 0
for line in lines:
    cmd = line.split()
    if cmd[0] == "forward":
        h += int(cmd[1])
        depth += (int(cmd[1]) * aim)
    if cmd[0] == "up":
        aim -= int(cmd[1])
    if cmd[0] == "down":
        aim += int(cmd[1])

print(h * depth)