class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        temp = [[0] * (len(grid[0])+2)]
        for line in grid:
            temp.append([0] + line + [0])
        temp.append([0] * (len(grid[0])+2))
        
        print(temp)
        perimeter = 0
        for i in range(1,len(temp)-1):
            for j in range(1,len(temp[0])-1):
                if temp[i][j] == 1:
                    neighbour = temp[i-1][j]+temp[i+1][j]+temp[i][j-1]+temp[i][j+1]
                    perimeter += 4-neighbour
                
        return perimeter
        
