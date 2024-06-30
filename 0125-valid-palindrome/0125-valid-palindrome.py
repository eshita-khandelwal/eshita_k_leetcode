class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res=""
        for a in s:
            if a.isalnum():
                res+=a.lower()
        
        i,j=0,len(res)-1
        print(res)
        while i<=j:
            if res[i]==res[j]:
                i+=1
                j-=1
            else:
                return False
        return True
