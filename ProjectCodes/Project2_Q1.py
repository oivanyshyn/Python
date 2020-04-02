nums = [-2, 0, 2, 3, 6, 7, 9]

nums.sort()
start = 0
end = len(nums) - 1

while start < end:
    if nums[start] > start:
        start = nums[start]
    elif nums[start] < start:
        start += 1
    elif nums[start] == start:
        print(f"{start}")
        start += 1