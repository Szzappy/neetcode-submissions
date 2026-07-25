class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            
            elif c == ')':
                if len(stack) == 0:
                    return False
                item = stack.pop()
                if item != '(':
                    return False
                continue
            
            elif c == '}':
                if len(stack) == 0:
                    return False
                item = stack.pop()
                if item != '{':
                    return False
                continue

            elif c == ']':
                if len(stack) == 0:
                    return False
                item = stack.pop()
                if item != '[':
                    return False
                continue

        if len(stack) == 0:
            return True

        return False
