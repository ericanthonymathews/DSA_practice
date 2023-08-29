class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = nums[0]
        num_sum = 0
        for number in nums:
            num_sum += number
            min_val = min(min_val, num_sum)
        res = (-(min_val) + 1)
        if res < 1:
            return 1
        else:
            return res
