def char_freq(s,q):
    #26 letters
    hash_list = [0] * 26
    #build frequency from string 's'
    for ch in s:
        ascii_val = ord(ch)
        index = ascii_val - 97
        hash_list[index]+=1
        
    # answer queries from string 'q'
    result = []
    for ch in q:
        ascii_val = ord(ch)
        index = ascii_val - 97
        result.append(hash_list[index])
    return result
    
s = "avfsadedw"
q="csdvsdfwdcw"
print(char_freq(s,q))