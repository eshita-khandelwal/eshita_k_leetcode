class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for i in magazine:
            count[i] = 1+count.get(i,0)
        for j in ransomNote:
            if count.get(j,0)>0:
                count[j]-=1
            else:
                return False
        return True