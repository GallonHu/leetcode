class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(',']':'[','}':'{'}
        for char in s:
            if char in mapping:
                front = stack.pop() if stack else '@'
                if mapping[char] != front:
                    return False
            else:
                stack.append(char)
        return not stack