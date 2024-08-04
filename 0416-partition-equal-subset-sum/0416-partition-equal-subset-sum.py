class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #time complexity by brute force is 2^n as we have to take decisssion as to take a element or not take an element. A dp problem and complexity with that is O(n * sum(nums)/2) ~ O(n*sum(nums)). we can use set for this problem
        if sum(nums)%2==1:
            return False

        dp = set()
        dp.add(0) #we choose no element
        target = sum(nums)//2
        for n in nums:
            nextDp = set()
            for j in dp:
                nextDp.add(j+n)
                nextDp.add(j)
            dp = nextDp
            if target in dp:
                return True
        return False

