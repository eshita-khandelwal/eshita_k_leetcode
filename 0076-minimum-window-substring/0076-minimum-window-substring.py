class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        countT,windowcount={},{}
        for i in t:
            countT[i]=1+countT.get(i,0)
        l = 0
        res=[-1,-1]
        reslen=float(inf)
        have,need=0,len(countT)
        for r in range(len(s)):
            c = s[r]
            #windowcount[c]=1+windowcount.get(c,0)
            if c in countT:
                windowcount[c]=1+windowcount.get(c,0)
                if countT[c]==windowcount[c]:
                    have+=1
            while have==need: #loop to find the minimum window and move left pointer by 1 towards right
                if r-l+1<reslen:
                    reslen = r-l+1
                    res = [l,r]
                if s[l] in windowcount:
                    windowcount[s[l]]-=1
                    if windowcount[s[l]]<countT[s[l]]:
                        have-=1
                l+=1
        
        return s[res[0]:res[1]+1] if reslen!=float('inf') else ""
            
            




