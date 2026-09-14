class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # create hashmap to store seen numbers and their indexes
        seen = {}

        # iterate through array
        for i in range(len(nums)):
                key = nums[i] # current number
                diff = target - key # calculate the complement needed to reach target

                # if the complement exists in our hashmap
                if diff in seen:
                    return [seen[diff], i] # return both indexes

                seen[key] = i # store current number and its index for future checks