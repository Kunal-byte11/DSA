#when constraints are large, we can use hashing to preprocess the data 
def freq_query(n,m):
    freq={}
    
    #build frequency
    
    for num in n:
        freq[num] = freq.get(num,0) +1
        
    # answer query
    
    result = []
    
    for query in m:
        result.apped(freq.get(query,0))
    return result
    
n = [1,4,5,6,4,3,2, 7,3]
m = [ 3,6,2,24,5,6,4,2111,8]
print(freq_query(n,m))

#if constrains 1<=n[i]<=10 we hash_list = [0]*11

def frequency_queries(n, m):
    hash_list = [0] * 11   # since 1 ≤ n[i] ≤ 10

    # Step 1: Build frequency from n
    for num in n:
        if 1 <= num <= 10:
            hash_list[num] += 1

    # Step 2: Answer queries from m
    result = []
    for num in m:
        if 1 <= num <= 10:
            result.append(hash_list[num])
        else:
            result.append(0)

    return result


n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

print(frequency_queries(n,m))


