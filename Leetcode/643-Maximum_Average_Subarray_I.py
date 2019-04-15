class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = sum(nums[:k])/k
        maxAvg = avg
        for i in range(k, len(nums)):
            avg += nums[i]/k
            avg -= nums[i-k]/k
            if avg > maxAvg:
                maxAvg = avg
        
        return maxAvg
