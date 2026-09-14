class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # create an array with 26 "empty" indexes
        count = [0] * 26

        # iterate through first string encoding each letter via it's ASCII value
        for char1 in s:
            count[ord(char1) - ord('a')] += 1

        # repeat previous step with second string
        for char2 in t:
            count[ord(char2) - ord('a')] -= 1

        # if both encodings match -> anagram
        if all(i == 0 for i in count):
            return True
            
        return False