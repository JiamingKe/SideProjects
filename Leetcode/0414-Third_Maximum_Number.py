import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums)<3:
            return max(nums)
        
        temp = []
        for val in nums:
            temp.append(-val)
            
        heapq.heapify(temp)
        
        heapq.heappop(temp)
        heapq.heappop(temp)
        return -heapq.heappop(temp)
