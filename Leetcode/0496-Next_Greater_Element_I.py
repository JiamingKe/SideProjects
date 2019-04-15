class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        for i in range(len(nums2)):
            flag = True
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    table[nums2[i]] = nums2[j]
                    flag = False
                    break

            if flag:
                table[nums2[i]] = -1
                
        result = []
        for val in nums1:
            result.append(table[val])
        
        return result
