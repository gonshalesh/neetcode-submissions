class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for word in strs:
            for char in word:
                output.append(f"{ord(char)}&")
            output.append("/&")
        
        return "".join(output)

    def decode(self, s: str) -> List[str]:
        current_number = ""
        current_word = ""
        output = []
        
        for char in s:
            if char.isdigit():
                current_number += char
                
            if char == "&":
                # Check if current_number has content (is truthy)
                if current_number:
                    current_word += chr(int(current_number))
                    current_number = ""
                    
            if char == "/":
                # Commit the current word to output regardless of content
                output.append(current_word)
                current_word = ""
                current_number = ""

        return output