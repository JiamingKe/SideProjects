class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        horizontal = []
        vertical = []
        total = 0
        
        for row in grid:
            vertical.append(max(row))
            
        for i in range(len(grid[0])):
            temp = []
            for row in grid:
                temp.append(row[i])
            horizontal.append(max(temp))
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total += min(vertical[i], horizontal[j]) - grid[i][j]
                
        return total
