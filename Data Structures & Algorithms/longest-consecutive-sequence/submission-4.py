class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums) # O(1) lookup; duplicates dropped automatically
        consecutive_size = 0

        for num in seen: # iterate unique values only
            if num - 1 not in seen: # skip numbers that aren't sequence starts
                length = 1
                while num + length in seen: # count how far the sequence extends
                    length += 1
                consecutive_size = max(consecutive_size, length) # keep the longest

        return consecutive_size
