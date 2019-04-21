class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lowerbound = 0
        upperbound = len(nums) - 1
        while lowerbound < upperbound:
            mid = int((lowerbound + upperbound)/2)
            if (upperbound - mid)%2 == 0:
                if nums[mid] == nums[mid+1]:
                    lowerbound = mid + 2
                    continue
                if nums[mid] == nums[mid-1]:
                    upperbound = mid - 2
                    continue
                return nums[mid]
            else:
                if nums[mid] == nums[mid+1]:
                    upperbound = mid - 1
                    continue
                if nums[mid] == nums[mid-1]:
                    lowerbound = mid + 1
                    continue
                return nums[mid]
        return nums[lowerbound]

