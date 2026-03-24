# # brute force 
# maxi = float("-inf")
# n = len(nums)

# for i in range(n):
#     total = 0

#     for j in range ( i , n):
#         total = total + nums[j]
#         maxi = max(maxi,total)

# return maxi 
# tc => o(n^2)
# SC => o(1)


#-------------------------------------------------------------------------------------------------------
# optimal :- Kadane algorithm

# n = len(nums)

# maxi = float("-inf")

# total = 0

# for i in range(n):
#     total = total + nums[i]
#     maxi = max(maxi, total)
#     if total< 0:
#         total = 0

# return maxi

# tc = > O(n)
# sc = > O(1)