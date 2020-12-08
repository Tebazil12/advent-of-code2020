with open("input", 'r') as f:

    nums = f.readlines()
    nums = [int(i) for i in nums]
    
#print(f"nums: {nums}")

nums.sort()

print(f"~~~ {nums}")

len_nums = len(nums)
stop_now = False

for start_n in range(len_nums):
    print(start_n)
    
    for end_n in range(len_nums-1, 0,-1):
        print(end_n)
    
        current_sum = nums[start_n] + nums[end_n]
        
        if current_sum == 2020:
            print(f"woo, numbers are {nums[start_n]} and {nums[end_n]}, which timesd is {nums[start_n] * nums[end_n]}")
            stop_now = True
            break
            
        elif current_sum < 2020:
            len_nums = end_n +1
            break
    if stop_now:
        break
