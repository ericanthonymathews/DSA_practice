class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                break

            if i > 0 and nums[i - 1] == n:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    triplets.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
        return triplets
