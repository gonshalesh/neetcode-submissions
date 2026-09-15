# Best space complexity, 1st submission uses more but still in linear time

class Solution:

    def encode(self, strs: List[str]) -> str:

        output = [] # create empty list for encoded output
        for word in strs: # iterate through each string in list
            output.append(f"{len(word)}#{word}") # create encoded string

        # each word looks like this after encoding
        # 4#word

        return "".join(output) # return encoded strings as one long string

    def decode(self, s: str) -> List[str]:
        words = [] # store each decoded word
        i = 0 # position of the start of each encoded word (which is also its length)

        while i < len(s): # process until we reach the end of the encoded string
            current_pound = s.index("#", i) # find the "#" dividing length from word
            word_length = int(s[i:current_pound]) # read the length number left of "#"

            word_start = current_pound + 1 # word begins immediately after "#"
            word_end = word_start + word_length # word ends after word_length characters

            words.append(s[word_start:word_end]) # extract the word and store it
            i = word_end # move to the length number of the next section

        return words # return all decoded words