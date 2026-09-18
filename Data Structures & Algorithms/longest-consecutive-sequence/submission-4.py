class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        consecutive_size = 0

        for num in seen:
            if num - 1 not in seen:          # only start counting at sequence beginnings
                length = 1
                while num + length in seen:
                    length += 1
                consecutive_size = max(consecutive_size, length)

        return consecutive_size
