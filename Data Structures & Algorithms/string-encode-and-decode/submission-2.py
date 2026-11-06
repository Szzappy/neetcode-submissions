class Solution:
    # better solution would not use é, maybe some kind of length check
    def encode(self, strs: List[str]) -> str:
        newString = ""
        for string in strs:
            for char in string:
                newString += chr(ord(char) + 1)

            newString += 'é'

        return newString
            

    def decode(self, s: str) -> List[str]:
        returnStrs = []
        currentString = ""
        for char in s:
            if char == 'é':
                returnStrs.append(currentString)
                currentString = ""

            else:
                currentString += chr(ord(char) - 1)
            

        return returnStrs
