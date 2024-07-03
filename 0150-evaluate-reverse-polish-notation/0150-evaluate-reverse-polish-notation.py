class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        action = {"+": add, "-": sub, "*": mul, "/": truediv}
        for i in tokens:
            if i!='+' and i!='-' and i!='*' and i!='/':
                stack.append(i)
            else:
                op1,op2=0,0
                if len(stack)>=2:
                    op2=int(float(stack.pop()))
                    op1=int(float(stack.pop()))
                stack.append(int(action[i](op1,op2)))

        return int(float(stack[-1]))

