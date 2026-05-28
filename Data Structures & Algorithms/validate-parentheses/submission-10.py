class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen={")":"(","}":"{","]":"["}

        for char in s:
            if char in closeToOpen: # closing bracket
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else: # Case where stack is empty
                    return False
            else:
                stack.append(char)

        return True if not stack else False

        