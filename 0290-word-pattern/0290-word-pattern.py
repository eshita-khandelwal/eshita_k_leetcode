class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict1={}
        dict2={}
        pat = s.split()
        if len(pattern)!=len(pat):
            return False
        for i in range(len(pattern)):
            if pattern[i] in dict1 and dict1[pattern[i]]!=pat[i]:
                print(pattern[i],pat[i])
                return False
            if pat[i] in dict2 and dict2[pat[i]]!=pattern[i]:
                return False
            dict1[pattern[i]]=pat[i]
            dict2[pat[i]]=pattern[i]
            
        
        return True