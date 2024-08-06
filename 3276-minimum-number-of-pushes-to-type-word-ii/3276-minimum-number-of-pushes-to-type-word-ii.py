class Solution:
    def minimumPushes(self, word: str) -> int:
        count = {}
        for w in word:
            count[w] = 1 + count.get(w,0)
        
        m = 8
        res=0
        f = 1
        count = sorted(count.items(),key=lambda x:x[1],reverse = True)

        for key,val in count:
            if m>0:
                m-=1
                res += f * val
            else:
                m = 7
                f+=1
                res+=f*val
        return res

