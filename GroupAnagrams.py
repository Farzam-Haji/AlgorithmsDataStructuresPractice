#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#example:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
strs = ["eat","tea","tan","ate","nat","bat"]
#hashmap 
def hashmap(arr):

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

print (hashmap(strs))