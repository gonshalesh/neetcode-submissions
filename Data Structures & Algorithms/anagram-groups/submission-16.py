# BEST SOLUTION: O(n * k) runtime, no sorting needed

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create empty dictionary — keys will be tuples, values will be lists of words
        anagram_map = {}

        # iterate through each word
        for word in strs:
            # create a fresh array of 26 zeros (one for each letter), reset every word
            char_count = [0] * 26 
            
            for char in word:
                # use ord() to get the index (a=0, b=1...) and increment that slot
                char_count[ord(char) - ord('a')] += 1
            
            # convert list to tuple so it can be used as a dictionary key (lists can't be keys)
            fingerprint = tuple(char_count)
            
            # check if this fingerprint is new — if so, create a new empty list for it
            if fingerprint not in anagram_map:
                anagram_map[fingerprint] = []
            
            # add current word to the list for this fingerprint (same fingerprint = anagram)
            anagram_map[fingerprint].append(word)

        # return just the grouped lists, dropping the tuple keys
        return list(anagram_map.values())
