with open("input", "r") as f:

    nums = f.readlines()
    nums = [int(i) for i in nums]

# print(f"nums: {nums}")

nums.sort()

print(f"~~~ {nums}")

len_nums = len(nums)
stop_now = False

for i in range(len_nums):
    # print(i)

    for j in range(len_nums):
        # print(j)
        for k in range(len_nums):

            current_sum = nums[i] + nums[j] + nums[k]

            if current_sum == 2020:
                print(
                    f"woo, numbers are {nums[i]} and {nums[j]} and {nums[k]}, which timesd is {nums[i] * nums[j] * nums[k]}"
                )
                stop_now = True
                break

        if stop_now:
            break

    if stop_now:
        break
