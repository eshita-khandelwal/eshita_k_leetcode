class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=0
        count={}
        for i in s1:
            count[i]=1+count.get(i,0)
        while l<len(s2) and r<len(s2):
            if s2[l] not in count:
                l+=1
            elif s2[l] in count:
                r = l 
                c2={}
                while r<len(s2) and s2[r] in count and r-l+1<=len(s1):
                    c2[s2[r]]=1+c2.get(s2[r],0)
                    r+=1
                if c2==count:
                    return True
                else:
                    l+=1
        
        return False

