class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        score = 0
        stack = []
        for i in range(len(S)):
            if S[i] == '(':
                stack.append(i)
                continue
            
            index = stack.pop()
            if len(stack) == 0:
                score += self.computeScore(S[index:i+1])
        return score
        
    def computeScore(self, S:str) -> int:
        if len(S) == 2:
            return 1
        return int(self.scoreOfParentheses(S[1:-1])*2)
