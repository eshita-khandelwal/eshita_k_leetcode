class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = {}
        sum1 = sum(nums)
        if sum1%2==1:
            return False
        target = sum1//2
        def part(i,s):
            if (i,s) in cache:
                return cache[(i,s)]
            if i==len(nums):
                if s!=target:
                    return False
                else:
                    return True
            if s == target:
                return True
            a = part(i+1,s+nums[i])
            if a:
                return True
            
            b = part(i+1,s)
            if b:
                return True
            cache[(i,s)] = False
            return cache[(i,s)]
        return part(0,0)
            
            