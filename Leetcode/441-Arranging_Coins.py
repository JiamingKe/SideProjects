class Solution:
    def arrangeCoins(self, n: int) -> int:
        total = 0
        row = 1
        while total <= n:
            total += row
            row += 1
        return row-2
