class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        while True:
            if stack and popped[0] == stack[-1]:
                stack.pop()
                popped = popped[1:]
            else:
                stack.append(pushed[0])
                pushed = pushed[1:]
            if len(pushed)==0 and len(popped)==0:
                return True
            elif popped and stack and popped[0] != stack[-1] and (len(pushed)==0 or len(popped)==0):
                return False
            