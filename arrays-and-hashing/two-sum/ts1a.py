class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments_hashmap = dict()
        for i in range(len(nums)):
            num = nums[i]
            compliment = target - num
            if compliment in compliments_hashmap:
                return [compliments_hashmap[compliment], i]
            else:
                compliments_hashmap[num] = i
        return None
