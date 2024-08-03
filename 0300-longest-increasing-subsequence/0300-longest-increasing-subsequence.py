class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #we have a choice to either take the number or do not take the number. this problem will be solved in o(n^2) we start from end and keep checking that what is th emax length of subseq from that position till the end.
        lis = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    lis[i]=max(lis[i],1+lis[j])
        return max(lis)