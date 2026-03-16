# first method 
nums=[5,-2,6,9,7]

nums[:] = nums[n-1] + nums[0:n-1]

# Alternate 
temp = nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1] = nums[i]

nums[0] = temp
