class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            curr_letters = [0] * 26
            for letter in string:
                curr_letters[ord(letter) - 97] += 1

            key = tuple(curr_letters)

            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(string)

        return list(anagrams.values())

