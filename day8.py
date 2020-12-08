with open("input-day8", "r") as f:

    lines = f.readlines()

for i, line in enumerate(lines):
    lines[i] = [line.split()[0], int(line.split()[1]), False]
# print(lines)

accumulator = 0
indexor  = 0

while True:
    if lines[indexor][2] == True:
        break

    if lines[indexor][0] == 'acc':
        lines[indexor][2] = True
        accumulator = accumulator + lines[indexor][1]
        indexor = indexor + 1

    elif lines[indexor][0] == 'jmp':
        lines[indexor][2] = True
        indexor = indexor + lines[indexor][1]

    elif lines[indexor][0] == 'nop':
        lines[indexor][2] = True
        indexor = indexor + 1


print(accumulator)

