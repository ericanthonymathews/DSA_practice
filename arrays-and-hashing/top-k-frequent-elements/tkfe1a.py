class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_count_dict = dict()
        k_frequent_elements = list()
        for num in nums:
            if num not in number_count_dict:
                number_count_dict[num] = 1
            else:
                number_count_dict[num] += 1
        sorted_number_count_tuples_list = sorted(
            number_count_dict.items(), key=lambda x: x[1])
        for i in range(k):
            value_and_count_tuple = sorted_number_count_tuples_list.pop()
            value = value_and_count_tuple[0]
            k_frequent_elements.append(value)
        return k_frequent_elements
