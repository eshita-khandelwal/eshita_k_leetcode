class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def isPal(s,i,j):
            for k in range(i,j+1):
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True

        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if isPal(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        dfs(0)
        return res
        