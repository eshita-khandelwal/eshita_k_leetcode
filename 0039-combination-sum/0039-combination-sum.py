class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #https://www.youtube.com/watch?v=GBKI9VSKdGg
        res = []
        subset = []
        def dfs(i):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            if i == len(nums) or sum(subset)>target:
                return
            
            subset.append(nums[i])
            dfs(i) #call the fuction with i, keep calling it
            subset.pop()
            dfs(i+1) #you dont need nums[i] ever again so now move to next element. 
        dfs(0)
        return res
