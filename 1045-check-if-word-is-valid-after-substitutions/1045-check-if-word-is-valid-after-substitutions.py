class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<3:
            return False
        stack=[]
        for i in s:
            stack.append(i)
            if len(stack)>=3:
                if stack[-1]=='c' and stack[-2]=='b' and stack[-3]=='a':
                    stack.pop()
                    stack.pop()
                    stack.pop()
        return not stack
            