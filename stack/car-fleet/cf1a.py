class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tuples = list(zip(position, speed))
        tuples.sort(reverse=True)
        stack = []
        for p, s in tuples:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
