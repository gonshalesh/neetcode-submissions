# BEST SOLUTION: O(n * k) runtime, no sorting needed

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {} # keys are fingerprints; values are lists of anagram words

        for word in strs: # process each word and reset counts for it
            char_count = [0] * 26 # fresh array of 26 zeros, one for each letter
            
            for char in word: # use ord() to find the letter's index and increment it
                char_count[ord(char) - ord('a')] += 1
            
            fingerprint = tuple(char_count) # tuple can be a dictionary key; lists cannot
            
            if fingerprint not in anagram_map: # create a bucket for a new fingerprint
                anagram_map[fingerprint] = []
            
            anagram_map[fingerprint].append(word) # same fingerprint means anagram

        return list(anagram_map.values()) # return groups without their fingerprint keys
