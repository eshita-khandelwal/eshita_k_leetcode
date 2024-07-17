class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #we use backtracking here. first we add an element then we pop an element. 
        res = []
        subset = []
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res