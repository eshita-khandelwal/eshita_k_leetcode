class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max1 = 0
        for i in s:
            if i-1 in s: continue
            j = 1
            while j + i in s:
                j+=1
            max1=max(max1,j)
        return max1
