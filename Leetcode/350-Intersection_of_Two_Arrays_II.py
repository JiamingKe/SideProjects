class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table1 = self.convert(nums1)
        table2 = self.convert(nums2)
        
        result = []
        for key in table1:
            if table2.get(key) is not None:
                result += [key] * min(table1[key], table2[key])
        
        return result
        
    def convert(self, nums: List[int]) -> dict:
        table = {}
        for val in nums:
            if table.get(val) is None:
                table[val] = 1
            else:
                table[val] += 1
        return table
