with open("input-day3", 'r') as f:

    # nums = f.readlines()
    # nums = [int(i) for i in nums]

# f=open('file.txt')
#     for i in list(f.read()):
#         print(i)
    line_length = None
    # all_nums = []
    num_trees = [0,0,0,0,0]
    num_free = 0
    for i, line in enumerate(f):
        line = line.strip()
        # print(line)
        # print(i)
        if line_length is None:
            line_length = len(line)



        for j ,step in enumerate([1,3,5,7, 1]):



            index_to_check = (i * step)%(line_length)

            # print(index_to_check)

            if line[index_to_check] == '#':
                if j == 4 and i%2 == 1:
                    pass
                else:
                    num_trees[j] = num_trees[j] + 1

        # line[index_to_check] = 'X'

        # new = list(line)
        # new[index_to_check] = 'X'
        # ''.join(new)
        #
        # print(new)
        # all_nums.append(num_trees)
product = num_trees[0]* num_trees[1]* num_trees[2]* num_trees[3]* num_trees[4]
print(f"Num trees {num_trees}, product {product}")
# print(nums)
