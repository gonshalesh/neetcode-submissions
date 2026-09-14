class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = [0] * 26

        for char1 in s:
            count[ord(char1) - ord('a')] += 1

        for char2 in t:
            count[ord(char2) - ord('a')] -= 1

        if all(i == 0 for i in count):
            return True
            
        return False