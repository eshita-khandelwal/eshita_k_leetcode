from functools import lru_cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        @lru_cache(maxsize=None)
        def dfs(o,c,i):
            if i==len(s):
                if o==c:
                    return True
                return False
            if c>o:
                return False
            if s[i]=='(':
                return dfs(o+1,c,i+1)
            if s[i]==')':
                return dfs(o,c+1,i+1)
            if s[i]=='*':
                return dfs(o+1,c,i+1) or dfs(o,c+1,i+1) or dfs(o,c,i+1)
        
        return dfs(0,0,0)
