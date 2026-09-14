class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # create set to store seen integers
        seen = set()

        # iterate through array
        for num in nums:

            # if current number exists in our set
            if num in seen:
                return True # duplicate found
            else:
                seen.add(num) # add the number to the set for future checks
        
        return False # no duplicates found if integers don't repeat
        