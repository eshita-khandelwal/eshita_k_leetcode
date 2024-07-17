class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []#current subset
        seen = set()

        def dfs(i):
            if i == len(nums):
                t = sorted(subset)
                t = tuple(t)
                if t not in seen:
                    res.append(subset.copy())
                    seen.add(t)
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res