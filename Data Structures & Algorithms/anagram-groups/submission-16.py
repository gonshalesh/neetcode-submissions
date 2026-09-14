# BEST SOLUTION: O(n * k) runtime, no sorting needed

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            # Create a count of 26 zeros (one for each letter)
            count = [0] * 26 
            
            for char in word:
                # Use ord() to get the index (a=0, b=1...)
                count[ord(char) - ord('a')] += 1
            
            # Use the TUPLE as the key (this is the "score" that never collides)
            key = tuple(count)
            
            if key not in groups:
                groups[key] = []
            
            groups[key].append(word)

        return list(groups.values())
