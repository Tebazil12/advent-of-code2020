with open("input-day3", 'r') as f:

    # nums = f.readlines()
    # nums = [int(i) for i in nums]

# f=open('file.txt')
#     for i in list(f.read()):
#         print(i)
    num_trees = 0
    num_free = 0
    line_length = None
    for i, line in enumerate(f):
        line = line.strip()
        # print(line)
        # print(i)
        if line_length is None:
            line_length = len(line)

        index_to_check = (i * 3)%(line_length)

        # print(index_to_check)

        if line[index_to_check] == '#':
            num_trees = num_trees + 1
        elif line[index_to_check] == '.':
            num_free = num_free +1
        else:
            raise NameError("what...")

        # line[index_to_check] = 'X'

        new = list(line)
        new[index_to_check] = 'X'
        ''.join(new)

        print(new)



        # for ch in line:
        #     if ch == chosen_ch:
        #         # print(ch)
        #         count_chs = count_chs +1
        # print(count_chs)
        #
        # if count_chs >= int(limits[0]) and count_chs <= int(limits[1]):
        #     num_valid = num_valid +1

print(f"Num trees {num_trees}, num free {num_free}")
# print(nums)
