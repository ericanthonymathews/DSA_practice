class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        c_min = float('inf')
        while l <= r:
            m = (l + r) // 2
            c_min = min(c_min, nums[m])

            if nums[m] > nums[r]:
                l = m + 1

            else:
                r = m - 1
        return c_min
