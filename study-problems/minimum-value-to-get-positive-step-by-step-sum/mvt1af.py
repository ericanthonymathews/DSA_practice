class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = nums[0]
        num_sum = 0
        for number in nums:
            num_sum += number
            min_val = min(num_sum, min_val)
        res = (-(min_val) + 1)
        if min_val == 1:
            return 0
        else:
            return res
