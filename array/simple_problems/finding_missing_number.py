# # # Brute Force 
# # nums=[9,6,4,2,3,5,7,0,1]
# # n=len(nums)

# # for i in range (0+ n+1):
# #     if i not in nums:
# #         return 1
    

# # TC=> o(n^2)
# # SC=>O(1)

# #better  
# n=len(nums),freq={}
# for i in range (0, n+1):
#     freq[i] = 0

# for num in nums:
#     freq[num] = 1

# for k,u in freq.items():
#     if u==0:
#         return k 
    

# # optimal soln
# nums = [7 , 6 , 4, 0 , 2 , 2 , 3 ]

# n=len(nums)
# original_total = (n*(n+1)) // 2
# return original_total - sum(nums)