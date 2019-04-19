class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}
        

    def insert(self, key: str, val: int) -> None:
        self.table[key] = val

    def sum(self, prefix: str) -> int:
        value = 0
        for key in self.table:
            if key[:len(prefix)] == prefix:
                value += self.table[key]
        
        return value

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
