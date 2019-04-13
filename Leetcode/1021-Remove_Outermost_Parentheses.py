class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = 0
        output = ""
        index = -1
        for i in range(len(S)):
            if S[i] == '(':
                stack += 1
                
                if stack == 1:
                    index = i
            else:
                stack -= 1
                
                if stack == 0:
                    output += S[index+1:i]

        return output
            
