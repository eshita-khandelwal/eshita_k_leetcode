class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        res=0
        cnt = 0
        l = 0
        m =1
        r = 2
        n = len(colors)
        for i in range(0,len(colors)):
            if  colors[(l+i)%n] == colors[(r+i)%n] and colors[(m+i)%n]!=colors[(l+i)%n]:
                res+=1

        return res


