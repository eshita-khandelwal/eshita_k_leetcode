class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0 #left pointer
        charset = set()
        res=0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            res = max(res,r-l+1)
        
        return res
            


