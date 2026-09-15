# Optimal linear solution, worst case O(n^2)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {} # dictionary to track how many times each number appears
    
        for num in nums: # build the frequency map — count occurrences of each number
            if num in freq_map:
                freq_map[num] += 1 # seen before, increment count
            else:
                freq_map[num] = 1 # first time seeing this number
        
        buckets = [[] for _ in range(len(nums) + 1)] # index = frequency; size handles max possible count

        for num, freq in freq_map.items(): # place each number into its frequency bucket
            buckets[freq].append(num)

        top_k = [] # collect the top k most frequent elements

        for i in range(len(buckets) - 1, -1, -1): # walk from highest frequency to lowest
            for num in buckets[i]: # grab every number in this frequency bucket
                top_k.append(num)
                if len(top_k) == k: # stop as soon as we have k elements
                    return top_k 