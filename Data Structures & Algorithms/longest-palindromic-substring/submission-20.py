class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None:
            return 0

        # dp1 is the length of palindrome at i where i is odd and centre
        # dp2 is length of palindrome at i where i is even and i + 1 is centre alongside it
        dp1 = 0 # 
        dp2 = 0

        longestDP = ""

        n = len(s)

        for i in range(n):
            dp1 = s[i]
            dp2 = s[i]

            checkEven = False
            checkOdd = True
            if i < n - 1 and s[i + 1] == s[i]:
                dp2 = dp2 + s[i + 1]
                checkEven = True

            for j in range(1, min(i + 1, n - i)):
                if checkOdd and s[i + j] == s[i - j]:
                    dp1 = s[i - j] + dp1 + s[i + j]
                
                else:
                    checkOdd = False

                if checkEven and j < n - i - 1 and s[i + j + 1] == s[i - j]:
                    dp2 = s[i - j] + dp2 + s[i + j + 1]

                else:
                    checkEven = False

            if len(dp1) > len(longestDP):
                longestDP = dp1

            if len(dp2) > len(longestDP):
                longestDP = dp2

        return longestDP