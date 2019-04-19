class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        for i in range(len(A)):
            if int("".join(str(x) for x in A[i]), 2) >= 2**(len(A[i])-1):
                A[i] = self.flipRow(A[i])
                
        for i in range(len(A[0])):
            temp = []
            for val in A:
                temp.append(val[i])
                
            if sum(temp) <= int(len(A)/2):
                temp = self.flipRow(temp)
                for j in range(len(A)):
                    A[j][i] = temp[j]
                    
        return self.computeMatrix(A)
        
    def flipRow(self, A: List[int]) -> List[int]:
        ans = []
        for val in A:
            if val == 1:
                ans.append(0)
            else:
                ans.append(1)
        return ans
    
    def computeMatrix(self, A: List[List[int]]) -> int:
        value = 0
        for val in A:
            value += int("".join(str(x) for x in val), 2)
        return value

