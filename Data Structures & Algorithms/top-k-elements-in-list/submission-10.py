# Optimal linear solution, worst case O(n^2)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create dictionary to track how many times each number appears
        freq_map = {}
    
        # build the frequency map — count occurrences of each number
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1 # seen before, increment count
            else:
                freq_map[num] = 1 # first time seeing this number
        
        # create buckets — index = frequency, value = list of numbers with that frequency
        # size is len(nums) + 1 because a number can appear at most len(nums) times
        buckets = [[] for _ in range(len(nums) + 1)]

        # place each number into the bucket matching its frequency
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        # collect the top k most frequent elements
        top_k = []

        # walk backwards from highest frequency to lowest
        for i in range(len(buckets) - 1, -1, -1):
            # grab every number in this frequency bucket
            for num in buckets[i]:
                top_k.append(num)
                # stop as soon as we have k elements
                if len(top_k) == k:
                    return top_k 