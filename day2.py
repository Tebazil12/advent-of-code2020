with open("input-day2", 'r') as f:

    # nums = f.readlines()
    # nums = [int(i) for i in nums]

# f=open('file.txt')
#     for i in list(f.read()):
#         print(i)
    num_valid = 0
    for line in f:
        print("new line")
        split_line = line.split()
        print(split_line)
        print(split_line[0])
        limits = split_line[0].split('-')
        print(limits)
        # print(int(limits[0]))
        # print(split_line[1].split(':'))

        chosen_ch = split_line[1][0]
        print(chosen_ch)

        count_chs = 0
        for ch in split_line[2]:
            if ch == chosen_ch:
                # print(ch)
                count_chs = count_chs +1
        print(count_chs)

        if count_chs >= int(limits[0]) and count_chs <= int(limits[1]):
            num_valid = num_valid +1

print(num_valid)
# print(nums)
