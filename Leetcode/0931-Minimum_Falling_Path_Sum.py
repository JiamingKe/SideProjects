class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        for i in range(1, len(A)):
            for j in range(0, len(A[0])):
                index = j-1
                if index < 0:
                    index = 0
                
                temp = A[i-1][index:j+2]
                A[i][j] += min(temp)
        
        return min(A[-1])
