class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            if self.matchPattern(word, pattern):
                ans.append(word)
        return ans
            
    def matchPattern(self, word: str, pattern: str) -> bool:
        if len(word) != len(pattern):
            return False
        
        table = {}
        for i in range(len(word)):
            if table.get(pattern[i]) is None:
                table[pattern[i]] = word[i]
            elif table[pattern[i]] != word[i]:
                return False
            
        tableArray = [table[key] for key in table]
        return len(tableArray) == len(set(tableArray))
        
