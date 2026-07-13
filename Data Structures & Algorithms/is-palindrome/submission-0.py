class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        while i < len(s):
            if ord(s[i]) < 48 or ord(s[i]) > 57 and ord(s[i]) < 97 or ord(s[i]) > 122:
                s = s[:i] + s[i+1:]
                i -= 1
            
            i += 1

        front = 0
        end = len(s) - 1

        while (front < end):
            if (s[front] != s[end]):
                return False 
            
            front += 1
            end -= 1

        return True
