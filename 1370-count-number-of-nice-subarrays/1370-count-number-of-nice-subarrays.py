class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #we are using three pointer approach. l,r,m. initially l=m=0. we will calculate elements in a window that satisfy the condition as l-m+1. once we are in the window we will see increment m pointer till the start of first odd element. then the number of subarrays that can we formed will be m-l+1
        l=m=0
        res = 0
        odd =0
        for r in range(len(nums)):
            odd +=nums[r]%2
            while odd>k:
                odd-=nums[l]%2
                l+=1
                m=l
            if odd == k:
                while nums[m]%2==0:
                    m+=1
                res+=m-l+1
        return res

