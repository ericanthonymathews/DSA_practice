class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_except_self_list = [1] * len(nums)
        for number_index in range(len(nums)):
            for product_index in range(len(product_except_self_list)):
                if product_index == number_index:
                    continue
                else:
                    product_except_self_list[product_index] *= nums[number_index]
        return product_except_self_list

# Failed due to time limit being exceeded. Worked on test cases
