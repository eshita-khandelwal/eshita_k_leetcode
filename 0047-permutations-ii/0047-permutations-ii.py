class Solution:
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        if len(nums)==1:
            return [nums.copy()]
        for i in range(len(nums)):
            n=nums.pop(0)
            perms = self.permuteUnique(nums)
            for p in perms:
                p.append(n)
                perm_tuple = tuple(p)
                if perm_tuple not in seen:
                    res.append(p)
                    seen.add(perm_tuple)
            
            #res.extend(perms)
            nums.append(n)
        return res
        
            