# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# ex:
# input:
nums = [3, 4, 2]
target = 6
# output:
# [1, 2]


#Brute Force
#time= O(n^2) space=O(1)
def TwoSum_BruteForce(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j and arr[i]+arr[j] == target:
                return [i, j]

# print(TwoSum_BruteForce(nums, target))


#Looking for the deficit in array
#time= O(n^2) space= O(1)
def TwoSum_2(arr, target):
    for i in range(len(arr)):
        deficit = target - nums[i]
        if deficit in nums and nums.index(deficit) is not i: #looking for a value in array has O(n) time complexity. unlike dict
            return [i, nums.index(deficit)]
        
# print (TwoSum_2(nums, target))


#hashmap
#time= O(n)  space= O(n)
def TwoSum_Hashmap(arr, target):
    hmap={} #key = number, value = index
    for i, n in enumerate (arr):
        deficit = target - n
        if deficit in hmap:
            return [i, hmap[deficit]]
        hmap[n] = i  #add after checking the hashmap so same index can't sum with itself. and because when we iterate over 2nd key, 1st already exist in map

# print (TwoSum_Hashmap(nums, target))
