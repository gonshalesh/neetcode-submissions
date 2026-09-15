class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_parts = [] # build the encoded string piece by piece

        for word in strs: # process each word in the input list
            for char in word: # process each character in the current word
                encoded_parts.append(f"{ord(char)}&")

            encoded_parts.append("/&") # mark the end of the current word

        return "".join(encoded_parts) # combine all encoded pieces into one string

    def decode(self, encoded_string: str) -> List[str]:
        code_point_digits = "" # digits for the current character's Unicode number
        current_word = "" # build the current decoded word one character at a time
        decoded_words = [] # store each completed word

        for char in encoded_string: # read the encoded string one character at a time
            if char.isdigit():
                code_point_digits += char

            if char == "&":
                if code_point_digits: # convert collected digits back into a character
                    current_word += chr(int(code_point_digits))
                    code_point_digits = ""

            if char == "/":
                decoded_words.append(current_word) # save the completed word, including empty words
                current_word = ""
                code_point_digits = ""

        return decoded_words