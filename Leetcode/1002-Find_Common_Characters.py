class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) == 0:
            return []
        
        table = self.convert(A[0])
        for word in A:
            newTable = {}
            temp = self.convert(word)
            for c in temp:
                if table.get(c) is not None:
                    newTable[c] = min(temp[c], table[c])
            table = newTable
        
        result = []
        for key in table:
            result += [key]*table[key]
        return result
    
    def convert(self, S: str) -> dict:
        table = {}
        for c in list(S):
            if table.get(c) is None:
                table[c] = 1
            else:
                table[c] += 1
        return table
