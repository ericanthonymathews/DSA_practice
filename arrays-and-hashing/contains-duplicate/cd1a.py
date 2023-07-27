class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_of_nums = set()
        for num in nums:
            if num not in set_of_nums:
                set_of_nums.add(num)
            else:
                return True
        return False
