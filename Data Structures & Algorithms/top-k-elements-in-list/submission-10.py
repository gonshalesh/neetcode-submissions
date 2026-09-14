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
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq_map.items():
            buckets[freq].append(num)

        top_k = []

        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k 