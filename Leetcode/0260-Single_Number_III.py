class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = set()
        for val in nums:
            if val not in ans:
                ans.add(val)
            else:
                ans.remove(val)
        return list(ans)

