class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0:
                break
            if i > 0 and nums[i - 1] == n:
                continue
            l, r = i + 1, len(nums) - 1
            while l != r:
                if l != i + 1 and nums[l] == nums[l - 1]:
                    l += 1
                if r != len(nums) - 1 and nums[r] == nums[r + 1]:
                    r -= 1
                if n + nums[l] + nums[r] < 0:
                    l += 1
                if n + nums[l] + nums[r] > 0:
                    r -= 1
                if n + nums[l] + nums[r] == 0:
                    triplets.append([n, nums[l], nums[r]])
        return triplets
