class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:     
        totalSum = sum(A)
        if totalSum % 3 != 0:
            return False

        target = totalSum / 3
        count = 0
        n = len(A)
        partSum = 0

        for i in range(n):
            partSum += A[i]

            if partSum == target:
                count += 1
                partSum = 0

        return count == 3
