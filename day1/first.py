print("Day one: how many number increases are there")
total = 0
f = open("input")
lines = f.readlines()
f.close()
previous = int(lines[0])
for line in lines:
    current = int(line)
    if current > previous:
        total += 1
    previous = current

print(total)