class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set() # store integers that have already appeared

        for num in nums: # iterate through the array

            if num in seen: # check whether the current number was already seen
                return True # duplicate found
            else:
                seen.add(num) # add the number to the set for future checks
        
        return False # no duplicates found if integers don't repeat
        