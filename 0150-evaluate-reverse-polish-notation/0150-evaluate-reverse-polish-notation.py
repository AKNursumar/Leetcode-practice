class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(t)
            else:
                l,r = int(stack.pop()),int(stack.pop())
                if t=="+":
                    stack.append(l+r)
                elif t=="-":
                    stack.append(r-l)
                elif t=="*":
                    stack.append(l*r)
                elif t=="/":
                    stack.append(r/l)
        return int(stack.pop())
        