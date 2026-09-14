class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            # 1. Use a dictionary for the inventory (Works for ANY character)
            inventory = {}
            for char in word:
                # No mapping needed! Just use the character itself as the key.
                inventory[char] = inventory.get(char, 0) + 1
            
            # 2. Sort the inventory items so anagrams match
            # This handles "" perfectly (it just becomes an empty tuple)
            key = tuple(sorted(inventory.items()))
            
            # 3. Standard Positive Logic
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())
