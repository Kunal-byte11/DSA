#brute force 
# n=len(nums)
# temp = []
# for i in range(0,n):
#     if nums[i]!=0:
#         temp.append(nums[i])

# nz=len(temp)

# for i in range(0,nz):
#     nums[i] = temp[i]

# for i in range(nz,n):
#     nums[i] = 0

# tc=>o(2n)~ O(n)
# cs=> O(m)

#------------------------------------------------------------------------------------------
#optimal Solution 

# if len(nums)==1:
#     return

# i=0

# while i < len(nums[i]):
#     if nums[i] == 0:
#         break
#     i+=1

# if i == len(nums[i]):
#     return

# j= i+1

# while j < len(nums[i]):
#     if nums[j] !=0:
#         nums[i],nums[j]=nums[j],nums[i]
#         i+=1

#     j+=1
