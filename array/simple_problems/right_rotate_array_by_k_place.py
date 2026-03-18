# nums=[2,4,5,3,2,4,6,4,2,]
#brute force 
# n = len(nums)
# rotation = k % n

# for _ in range(0,rotation):
#     e = nums.pop()
#     nums.insert(0,e)

# -------------------------------------------------------------------
#  using slicing
# nums=[2,4,5,3,2,4,6,4,2,]

# n = len(nums)
# nums[:] = nums[n-k:] + nums[:n-k]
#-------------------------------------------------------------------------------
# optimal way
# def reverse(nums,left,right):
#     while left < right:
#         nums[left],nums[right] = nums[right],nums[left]
#         left+=1
#         right-=1


# reverse(n-k,n-1)
# reverse(0,n-k-1)
# reverse(0,n-1)
# TC=o(n)
# SC=o(1)