import copy

with open("input-day8", "r") as f:

    lines = f.readlines()

for i, line in enumerate(lines):
    lines[i] = [line.split()[0], int(line.split()[1]), False]

lines.append(['eof'])
print(lines)


found = False
for i, line in enumerate(lines):
    iterate = True

    if found:
        break

    print(f"{i} time around loop")
    new_lines = copy.deepcopy(lines)
    if line[0] == 'jmp':
        # print(new_lines[i][0])
        new_lines[i][0] = 'nop'
        # print(new_lines[i][0])
    elif line[0] == 'nop':
        # print(new_lines[i][0])
        new_lines[i][0] = 'jmp'
        # print(new_lines[i][0])
    else:
        iterate = False

    # print(new_lines)
    # print(iterate)

    accumulator = 0
    indexor  = 0

    if iterate:

        while not found:
            if new_lines[indexor][0] == 'eof':
                # print(f"found")
                found = True
                break

            if new_lines[indexor][2] == True:
                break

            if new_lines[indexor][0] == 'acc':
                new_lines[indexor][2] = True
                accumulator = accumulator + new_lines[indexor][1]
                indexor = indexor + 1

            elif new_lines[indexor][0] == 'jmp':
                new_lines[indexor][2] = True
                indexor = indexor + new_lines[indexor][1]

            elif new_lines[indexor][0] == 'nop':
                new_lines[indexor][2] = True
                indexor = indexor + 1

            else:
                raise NameError("errrr")



print(f"accumulator {accumulator}")

