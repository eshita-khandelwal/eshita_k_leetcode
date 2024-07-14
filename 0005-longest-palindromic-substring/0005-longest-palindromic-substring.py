class Solution:
    def longestPalindrome(self, s: str) -> str:
        #expand the strings outwards. start from the i =0,l,r are set to i , for even length l=i and r=i+1
        len1 = len(s)
        lenmax = 0
        res=""
        for i in range(len1):
            l,r=i,i
            while l>=0 and r<len1 and s[l]==s[r]:
                if lenmax<r-l+1:
                    lenmax = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
            
            l,r=i,i+1
            
            while l>=0 and r<len1 and s[l]==s[r]:
                if lenmax<r-l+1:
                    lenmax = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
            
        return res
            
