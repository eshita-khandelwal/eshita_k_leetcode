class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() #sorting it becasue we need to remove duplicates
        res = []
        subset = []
        def backtrack(i,prev,sum1):
            if sum1 == target:
                res.append(subset.copy())
                return
            if sum1>target or i==len(nums):
                return
            if prev!=nums[i]:
                subset.append(nums[i]) #append to the list only if the previous element is not same
                backtrack(i+1,-1,sum1+nums[i]) #no previous here
                subset.pop()
            backtrack(i+1,nums[i],sum1) #sending a prev so that we can ignore it and not adding it to the sum
        backtrack(0,-1,0)
        return res