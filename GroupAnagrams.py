#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#example:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


#character frequency counting / frequency-based hashing
#time= O(k.n)  space= O(k.n) / n = max number of words k = max letters 
def CharacterFrequency(arr):

    hmap = {}

    for word in arr:
        letters = [0] * 26
        for char in word:
            letters[ord(char) - ord("a")] += 1
        key = tuple(letters)
        if key in hmap:
            hmap[key].append(word)
        else:
            hmap[key]= [word]

    return list(hmap.values())

# print (CharacterFrequency(strs))


#sort and hashmap
#time = O(n.k logk)  space = O(n.k)
def Sort(arr):
    
    hmap = {}

    for word in arr:
        sorted_word = ''.join(sorted(word))
        if sorted_word in hmap:
            hmap[sorted_word].append(word)
        else:
            hmap[sorted_word] = [word]

    return list(hmap.values())

# print(Sort(strs))