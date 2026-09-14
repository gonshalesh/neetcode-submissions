class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        result = []
        
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        for j in range(k):
            current_max = max(count, key=count.get)
            result.append(current_max)
            count.pop(current_max)
        
        return result