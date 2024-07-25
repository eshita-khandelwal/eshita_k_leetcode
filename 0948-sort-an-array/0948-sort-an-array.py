class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n<2:
            return nums[:]
        else:
            mid = n//2
            left = self.sortArray(nums[:mid])
            right = self.sortArray(nums[mid:])
            return self.merge(left,right)
    
    def merge(self,left,right):
        res = []
        i,j=0,0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        while i<len(left):
            res.append(left[i])
            i+=1
        while j<len(right):
            res.append(right[j])
            j+=1
        return res
        
