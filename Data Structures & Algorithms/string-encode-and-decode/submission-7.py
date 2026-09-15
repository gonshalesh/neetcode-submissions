class Solution:

    def encode(self, strs: List[str]) -> str:
        # create a list to build the encoded string piece by piece
        encoded_parts = []

        # process each word in the input list
        for word in strs:
            # process each character in the current word
            for char in word:
                # convert the character to its Unicode number and mark its end with '&'
                encoded_parts.append(f"{ord(char)}&")

            # mark the end of the current word with '/&'
            encoded_parts.append("/&")

        # combine all encoded pieces into one string
        return "".join(encoded_parts)

    def decode(self, encoded_string: str) -> List[str]:
        # temporarily store the digits for the current character's Unicode number
        code_point_digits = ""
        # build the current decoded word one character at a time
        current_word = ""
        # store each completed word
        decoded_words = []

        # read the encoded string one character at a time
        for char in encoded_string:
            # digits belong to the current character's Unicode number
            if char.isdigit():
                code_point_digits += char

            # '&' marks the end of either a character number or a word delimiter
            if char == "&":
                # if digits were collected, convert the number back into a character
                if code_point_digits:
                    current_word += chr(int(code_point_digits))
                    code_point_digits = ""

            # '/' marks the end of a word
            if char == "/":
                # save the completed word, including an empty word if there is one
                decoded_words.append(current_word)
                current_word = ""
                code_point_digits = ""

        return decoded_words