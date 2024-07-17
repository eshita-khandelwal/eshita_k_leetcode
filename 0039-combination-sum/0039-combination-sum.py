class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            if i == len(nums) or sum(subset)>target:
                return
            
            subset.append(nums[i])
            dfs(i)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
