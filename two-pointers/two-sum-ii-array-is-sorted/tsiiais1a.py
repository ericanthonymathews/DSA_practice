class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r, t = 0, len(numbers) - 1, target
        while l < r:
            if numbers[l] + numbers[r] < t:
                l += 1
            elif numbers[l] + numbers[r] > t:
                r -= 1
            else:
                return [l + 1, r + 1]
