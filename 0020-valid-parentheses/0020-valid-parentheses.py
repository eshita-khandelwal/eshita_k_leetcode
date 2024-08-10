class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                if stack:
                    if i == ')':
                        if stack[-1]=='(':
                            stack.pop()
                        else:
                            return False
                    elif i == '}':
                        if stack[-1]=='{':
                            stack.pop()
                        else:
                            return False
                    elif i == ']':
                        if stack[-1]=='[':
                            stack.pop()
                        else:
                            return False

        print(stack)
        return True if len(stack)==0 else False