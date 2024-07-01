class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        n = len(s)
        stack=[]
        while i<n:
            if s[i]=='(':
                stack.append(')')
            elif s[i]=='{':
                stack.append('}')
            elif s[i]=='[':
                stack.append(']')
            elif len(stack)==0 or stack.pop()!=s[i]:
                return False
            i+=1
        
        return len(stack)==0