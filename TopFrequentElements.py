# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
nums = [1,1,1,2,2,3]
k = 2

#hashmap sort
#time = O(n logn)
def one(arr, num):

    hashmap = {}
    for i in arr:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    hashset = [values for values in hashmap.values()]
    hashset.sort(reverse=True)
    chosen_values = hashset[:num]
    return [key for key in hashmap.keys() if hashmap[key] in chosen_values]

# print (one(nums,k))


#bucketsort hashmap
#time= O(n) space= O(n)
def two(arr, num):
    hashmap = {}
    frequnecy = [[] for i in range(len(arr)+1)]

    for i in arr:
        hashmap[i] = hashmap.get(i, 0) + 1
    for k, v in hashmap.items():
        frequnecy[v].append(k)   # freqency[v] would be the list that contain all the keys with same occurence

    res = []
    for i in range(len(frequnecy)-1, 0, -1):
        for j in frequnecy[i]:
            res.append(j)
            if len(res) == num:
                return res
            
# print(two(nums, k))