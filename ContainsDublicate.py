#Given an integer array nums, return True if any value appears at least twice in the array, and
#return False if every elemnt is distinct

#ex
#input: nums = [1,2,3,1]
#output: True

#bruteforce
#time = O(n**2)  space = O(1)
def ContainDublicat_BruteForce(arr: list):
    for i in range(len(arr)):
        if arr[i] in arr[:i] or arr[i] in arr[i+1:]:
            return True
    return False
# print (ContainDublicat_BruteForce(nums))


#sorting
#time = O(n logn)  Space= O(1)
def ContainDuplicate_Sorting(arr: list):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return True
    return False
# print (ContainDuplicate_Sorting(nums))


#HashSet
#time= O(n)  Space= O(n)
def ContainDublicat_HashSet(arr: list):
    hashset= set()
    for i in arr:
        if i in hashset:
            return True
        hashset.add(i)
    return False
# print (ContainDublicat_HashSet(nums))