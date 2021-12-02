print("Day one: how many number increases are there")
previoussum = 9999
total = 0
f = open("input")
lines = f.readlines()
f.close()
for i in range(1,len(lines)-1):
    current = int(lines[i])
    previous = int(lines[i-1])
    next = int(lines[i+1])
    currentsum = previous + current + next
    if currentsum > previoussum:
        total += 1
    previoussum = currentsum

print(total)