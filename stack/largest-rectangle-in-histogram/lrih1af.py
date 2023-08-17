class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0

        def find_largest_rectangle(lengths):
            stack = []
            while len(lengths):
                length = lengths.pop()
                stack.append(length)
                if len(stack) * min(stack) > res:
                    res = len(stack) * min(stack)
                find_largest_rectangle(lengths)
            return
        find_largest_rectangle(heights)
        return res
