def second_largest(nums=[]):
    l_value = float("-inf")
    s_value = float("-inf")

    for i in range (0 , n):
        if nums[i] > l_value:
            s_value = l_value
            l_value=nums[i]

        elif nums[i] > s_value and nums[i] != l_value:
            s_value=nums[i]

    return s_value


# comment
    
    


