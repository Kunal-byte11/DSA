# # brute force 
# n = len(nums)
# for i in range(0, n-1):
#     for j in range(i+1, n):
#         if nums[i] + nums[j] == target:
#             return [i,j]
# TC- O(n^2)
# SC- O(1)

# ----------------------------------------------------------------------------------------
# Optimal SOlution using dictinaary 
# n = len(nums)
# hash_map = {}

# for i in range (0 , n):
#     remaining = target- nums[i]
#     if remaining in hash_map:
#         return [hash_map[remaining], i]
    
#     hash_map[nums[i]] = i


# TC=> O(n)
# SC = > O(n)