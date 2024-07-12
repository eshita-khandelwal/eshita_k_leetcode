class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r,l=0,0
        q = collections.deque()
        res=[]
        while r in range(len(nums)):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            if q[0]==r-k:
                q.popleft()
            if r-l+1==k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res

