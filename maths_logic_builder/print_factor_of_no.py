brute force approach to find the factors of a number 
tc: O(n)
sc: O(k) in worst case when the number is prime and has only 2 factors, where k is the number of factors
def areFactor(num):
    result = []

    for i in range (1, num+1):
        if num% i == 0:
            result.append(i)

    return result
print(areFactor(67))
optimized approach to find the factors of a number
tc: O(n//2) = O(n)
sc: O(k) in worst case when the number is prime and has only 2 factors, where k is the number of factors

def areFactors(num):
    result = []
    
    for i in range (1, num//2 + 1):
        if num % i == 0:
            result.append(i)
    result.append(num)
        
    return result
    
print(areFactors(67))


optimized approach to find the factors of a number
tc: O(sqrt(n))
sc: O(k) in worst case when the number is prime and has only 2 factors, where k is the number of factors
from math import sqrt
def areFactors(num):
    result = []
    for i in range (1 , int(sqrt(num))+1):
        if num % i == 0:
            result.append(i)
        if num // i != i:
            result.append(num//i)
            
    result.sort()
    return result
print(areFactors(267))
