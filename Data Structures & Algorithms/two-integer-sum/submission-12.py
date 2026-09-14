class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i in range(len(nums)):
                key = nums[i]
                diff = target - key

                if diff in seen:
                    return [seen[diff], i]

                seen[key] = i