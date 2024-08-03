class Solution:
    def countSubstrings(self, s: str) -> int:
        #expand the string outward. for loop is for the entire string and we have to calculate for odd length and even length
        res = 0
        for i in range(len(s)):
            r=l=i
           
            while l>=0 and r<len(s) and s[l]==s[r]: #calculates odd length
               
                l-=1
                r+=1
                res+=1
            r=i+1
            l=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
                res+=1
        return res
            
