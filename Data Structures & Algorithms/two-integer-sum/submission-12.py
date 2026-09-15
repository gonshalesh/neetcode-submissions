class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {} # hashmap to store seen numbers and their indexes

        for i in range(len(nums)): # iterate through the array
            key = nums[i] # current number
            diff = target - key # calculate the complement needed to reach target

            if diff in seen: # check if the complement exists in the hashmap
                return [seen[diff], i] # return both indexes

            seen[key] = i # store current number and its index for future checks