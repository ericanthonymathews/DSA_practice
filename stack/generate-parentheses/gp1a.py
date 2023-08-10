class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def generate_possibilities(open_n: int, closed_n: int):
            if open_n == closed_n == n:
                res.append("".join(stack))
                return
            if open_n < n:
                stack.append('(')
                generate_possibilities(open_n + 1, closed_n)
                stack.pop()
            if closed_n < open_n:
                stack.append(')')
                generate_possibilities(open_n, closed_n + 1)
                stack.pop()

        generate_possibilities(0, 0)
        return res
