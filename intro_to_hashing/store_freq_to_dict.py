nums = [2, 3, 4, 5, 6,7 ,7 ,8 ,6, 4, 2, 3,4 ,6,6 ,7,76 ,70]

n = len(nums)
hash_map ={}

for i in range(0 , n):
    hash_map[nums[i]] = hash_map.get(nums[i] , 0) + 1
    
print(hash_map)

    
