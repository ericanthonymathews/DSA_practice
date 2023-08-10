class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t != "+"\
                    and t != "-"\
                    and t != "*"\
                    and t != "/":
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l + r)
                if t == "-":
                    stack.append(l - r)
                if t == "*":
                    stack.append(l * r)
                if t == "/":
                    stack.append(int(l / r))
        return stack.pop()
