import heapq
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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
