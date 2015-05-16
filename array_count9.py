def array_count9(nums):
    j = 0 
    if len(nums) < 4:
        z = len(nums)
    else: 
        z = 4
    for i in range(z):
        if nums[i] == 9:
            j += 1

    print j

array_count9([1, 2, 3, 4, 5, 9, 7, 5, 6, 9])
