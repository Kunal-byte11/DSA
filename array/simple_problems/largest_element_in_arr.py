def largest(nums):
    nums = [55,32,-97,3, 67]

    n = len(nums)
    largest_value = float("-inf")

    for i in range (0 , n ):
        largest_value = max(largest_value,nums[i])

    print(largest_value)

