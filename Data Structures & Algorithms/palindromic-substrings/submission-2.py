class Solution:
    def countSubstrings(self, s: str) -> int:
        if s is None:
            return 0

        n = len(s)
        # 2 cases, even and odd
        # 'aaa' => a, a, a, aa, aa, aaa
        numPalindromes = 0

        for i in range(n):
            checkOdd = True
            checkEven = True
            for j in range(min(i + 1, n - i)):
                if checkOdd and s[i + j] == s[i - j]:
                    numPalindromes += 1
                
                else:
                    checkOdd = False

                if checkEven and i + j + 1 < n and s[i + j + 1] == s[i - j]:
                    numPalindromes += 1

                else:
                    checkEven = False

                if not (checkOdd or checkEven):
                    break

        return numPalindromes

