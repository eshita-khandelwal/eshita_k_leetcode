class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #we are using backtracking https://www.youtube.com/watch?v=s7AvT7cGdSo&t=506s
        #[1,2,3]-> we first remove 1 then we have [2,3] so now we will have [2,3],[3,2] after we get the permutations we add back one to the nums at the end as well as in the permutations we got. this is the basic idea
        res =[] #final answer variable
        #base case
        if len(nums)==1:
            return [nums.copy()] # only one element now so we have to return it
        for i in range(len(nums)):
            n = nums.pop(0) #remove the element and find all combos without it
            perms = self.permute(nums) #if we remove 1 we get[2,3],[3,2]
            for p in perms:
                p.append(n) #[2,3,1], [3,2,1]
            res.extend(perms)
            nums.append(n) #nums is now [2,3,1]
        return res

       

