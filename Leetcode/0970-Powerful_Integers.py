import math
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        xList = [1]
        if x > 1:
            xList += [x**i for i in range(1, int(math.log(bound, x))+1)]
        yList = [1]
        if y > 1:
            yList += [y**i for i in range(1, int(math.log(bound, y))+1)]
                 
        result = []
        for xVal in xList:
            for yVal in yList:
                if xVal + yVal <= bound:
                    result.append(xVal + yVal)
                else:
                    break
        return list(set(result))
