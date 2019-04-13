class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1],[1,1]]
        if numRows == 0:
            return []
        elif numRows == 1:
            return output[:1]
        
        rowIndex = 1
        while numRows > 2:
            temp = [1]
            for i in range(len(output[rowIndex])-1):
                temp.append(output[rowIndex][i]+output[rowIndex][i+1])
            temp.append(1)
            output.append(temp)
            numRows -= 1
            rowIndex += 1
        return output
