# O(n * k) solution using some brute forcing

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {} # dictionary to track how many times each number appears
        top_k = [] # list to store our final answer
        
        for num in nums: # build the frequency map — count occurrences of each number
            if num in freq_map:
                freq_map[num] += 1 # seen before, increment count
            else:
                freq_map[num] = 1 # first time seeing this number
        
        for _ in range(k): # repeat k times to find the k most frequent elements
            most_frequent = max(freq_map, key=freq_map.get) # find key with highest count
            top_k.append(most_frequent) # add it to our answer
            freq_map.pop(most_frequent)
        
        return top_k 