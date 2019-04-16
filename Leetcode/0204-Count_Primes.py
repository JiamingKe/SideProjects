class Solution:
    def countPrimes(self, n: int) -> int:
        # Sieve of Eratosthenes
        if n < 2:
            return 0
        
        table = [1] * n
        table[0] = 0
        table[1] = 0
        for i in range(2, n):
            if table[i] == 0:
                continue
            
            for j in range(i**2, n, i):
                table[j] = 0
            
        return sum(table)
