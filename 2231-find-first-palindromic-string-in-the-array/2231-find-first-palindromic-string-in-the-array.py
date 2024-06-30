class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for w in words:
            i=0
            j=len(w)-1
            flag=0
            while i<=j:
                if w[i]==w[j]:
                    i+=1
                    j-=1
                else:
                    flag=1
                    break
            if flag==0:
                return w
        return ""
            
