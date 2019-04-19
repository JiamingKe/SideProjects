class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        table = {}
        for t in time:
            if t%60 != 0:
                if table.get(60 - t%60) is not None:
                    count += table[60 - t%60]
            else:
                if table.get(0) is not None:
                    count += table[0]
                
            if table.get(t%60) is None:
                table[t%60] = 1
            else:
                table[t%60] += 1

        return count
