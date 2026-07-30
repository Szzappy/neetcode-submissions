class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hashmap storing current substring letters
        longest = {}
        arr_longest = []
        max_len = 0
        l = 0
        for r in range(len(s)):
            print(r)
            if s[r] not in longest:
                longest[s[r]] = 1

            else:
                max_len = len(longest) if max_len < len(longest) else max_len

                if s[l] == s[r]:
                    del(longest[s[l]])
                    l += 1
                    longest[s[r]] = 1
                    continue
                    
                while s[l] != s[r]:
                    del(longest[s[l]])
                    l += 1
                
                del(longest[s[l]])
                l += 1
                
                longest[s[r]] = 1
                #longest = {c: 1}

        print(longest)
        max_len = len(longest) if max_len < len(longest) else max_len
        return max_len