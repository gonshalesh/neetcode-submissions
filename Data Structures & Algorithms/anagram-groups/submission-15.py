class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # map each frequency signature to its anagram words

        for word in strs: # process each word
            inventory = {} # count each character; works for any character
            for char in word: # use the character itself as the dictionary key
                inventory[char] = inventory.get(char, 0) + 1
            
            key = tuple(sorted(inventory.items())) # sorted signature makes anagrams match
            
            if key in groups: # append to the existing anagram group
                groups[key].append(word)
            else: # create a new anagram group
                groups[key] = [word]

        return list(groups.values())
