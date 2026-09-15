class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = [0] * 26 # create an array with 26 "empty" indexes

        for char1 in s: # encode each letter in the first string via its ASCII value
            count[ord(char1) - ord('a')] += 1

        for char2 in t: # subtract each letter in the second string
            count[ord(char2) - ord('a')] -= 1

        if all(i == 0 for i in count): # all zeroes means both encodings match
            return True
            
        return False