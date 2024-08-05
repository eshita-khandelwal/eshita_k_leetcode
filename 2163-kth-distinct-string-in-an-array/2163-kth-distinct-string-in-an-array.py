class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}
        for a in arr:
            count[a] = 1+count.get(a,0)
        for key,val in count.items():
            if val == 1:
                k-=1
            if k==0:
                return key
        return ''