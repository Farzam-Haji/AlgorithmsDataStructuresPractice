# Given two strings s and t, return true if the two strings are anagrams of each other, 
# otherwise return false.

# ex:
# Input: s = "racecar", t = "carrace"
# Output: true


#sort
#time= O(nlog n) space= O(n)
def sort(str1, str2):
    return sorted(str1) == sorted(str2) 
# print (sort(s, t))

#hashmap
#time= O(n) Sapce = O(n)
def hashmap(str1, str2):
    if len(str1) != len(str2):
        return False
    
    hashmapS, hashmapT = {}, {}
    for i in range(len(str1)):
        hashmapS[str1[i]] = 1 + hashmapS.get(str1[i], 0)
        hashmapT[str2[i]] = 1 + hashmapT.get(str2[i], 0)

    for key in hashmapS:
        if hashmapS[key] != hashmapT.get(key, 0):
            return False
    return True
# print (hashmap(s, t))

#frequency check
#time= O(n)  space= O(n)
def frequency_check(str1, str2):
    if len(str1) != len(str2):
        return False
    
    freq = {}
    for i in str1:
        freq[i] = freq.get(i, 0) + 1

    for j in str2:
        if j not in freq or freq[j] == 0 :
            return False
        freq[j] -= 1
    
    return all(value == 0 for value in freq.values())
# print (frequency_check(s, t))