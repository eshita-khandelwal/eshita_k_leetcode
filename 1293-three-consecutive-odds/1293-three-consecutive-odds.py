class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        l=0
        r =0 
        while r<len(arr):
            print(l,r)
            if arr[r]%2==1:
                if r-l+1 == 3:
                    return True
                r+=1
            else:
                l = r = r+1
        return False
