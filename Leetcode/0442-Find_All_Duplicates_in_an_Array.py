class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for val in nums:
            if nums[abs(val)-1] < 0:
                ans.append(abs(val))
            else:
                nums[abs(val)-1] *= -1
        return ans

