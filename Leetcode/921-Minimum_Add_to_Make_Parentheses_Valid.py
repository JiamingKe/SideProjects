class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        count = 0
        stack = 0
        for char in S:
            if char == '(':
                stack += 1
            elif stack > 0:
                stack -= 1
            else:
                count += 1
        
        if stack != 0:
            count += stack
        return count

