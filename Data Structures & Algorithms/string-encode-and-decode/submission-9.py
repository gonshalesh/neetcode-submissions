# Best space complexity, 1st submission uses more but still in linear time

class Solution:

    def encode(self, strs: List[str]) -> str:
        output = [] # create empty list for encoded output
        for word in strs: # iterate through each string in list
            output.append(f"{len(word)}#{word}") # create encoded string

        return "".join(output) # return encoded strings as one long string

    def decode(self, s: str) -> List[str]:
        output = [] # store each decoded string
        i = 0 # current position in the encoded string

        while i < len(s): # process strings until reaching the end
            separator = s.index("#", i) # find where the length ends
            length = int(s[i:separator]) # convert the length from text to an integer

            start = separator + 1 # string starts after the "#"
            end = start + length # string ends after its specified length

            output.append(s[start:end]) # extract and store the current string
            i = end # move to the start of the next encoded string

        return output # return all decoded strings