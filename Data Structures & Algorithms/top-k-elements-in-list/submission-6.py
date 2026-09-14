class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create dictionary to track how many times each number appears
        freq_map = {}
        # list to store our final answer
        top_k = []
        
        # build the frequency map — count occurrences of each number
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1 # seen before, increment count
            else:
                freq_map[num] = 1 # first time seeing this number
        
        # repeat k times to find the k most frequent elements
        for _ in range(k):
            # find the key with the highest value (most occurrences) in freq_map
            most_frequent = max(freq_map, key=freq_map.get)
            # add it to our answer
            top_k.append(most_frequent)
            # remove it so the next max() finds the next most frequent
            freq_map.pop(most_frequent)
        
        return top_k 