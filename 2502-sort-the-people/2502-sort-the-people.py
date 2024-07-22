class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = list(zip(names,heights))
        
        h = sorted(l,key=lambda x:x[1],reverse = True)
        res=[]

        for i in range(len(h)):
            res.append(h[i][0])
        return res
