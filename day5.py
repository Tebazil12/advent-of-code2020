def to_decimal(binary):
    reversed = binary[::-1]
    # print(reversed)
    count = 0
    for i, char in enumerate(reversed):
        if char == 'F' or char == 'L':
            bit = 0
        elif char == 'B' or char == 'R':
            bit = 1
        else:
            raise NameError(f"thats not B, F, L or R : {char}")
        count = count + (bit*(2**i))
    return count

with open("input-day5", 'r') as f:



    old_highest = 0
    all_ids = []
    for i, line in enumerate(f):
        line = line.strip()
        # print(line)
        # print(i)

        #take off last 3 chrs
        col_num_str = line[-3:] # last 3 chs
        col_num = to_decimal(col_num_str)
        print(col_num)

        row_num_str = line[:-3]
        row_num = to_decimal(row_num_str)
        print(row_num)

        seat_id = row_num*8 +col_num
        print(seat_id)
        if seat_id > old_highest:
            old_highest = seat_id
        all_ids.append(seat_id)

        # num_thing = to_decimal('FBFBBFF')
        # print(num_thing)
        # num_thing = to_decimal('RLR')
        # print(num_thing)

print(old_highest)
print(all_ids)
all_ids.sort()
print(all_ids)
offset = all_ids[0]
for i, id in enumerate(all_ids):
    if id != offset+i:
        print(f"{id-1} id")
        break



# print(nums)
