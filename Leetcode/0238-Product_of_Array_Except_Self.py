class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        for val in nums:
            ans.append(ans[-1]*val)
            
        right = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= right
            right *= nums[i]
        return ans[:-1]

