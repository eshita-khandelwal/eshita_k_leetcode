class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # you have to find from the end a break point such that a[i]<a[i+1]. after getting a break point index, compare from the remaining numbers which index is imediately greater swap it then reverse the remaining array. https://www.youtube.com/watch?v=JDOXKqF60RQ&t=792s
        #https://takeuforward.org/data-structure/next_permutation-find-next-lexicographically-greater-permutation/
        ind=-1
        
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind = i
                break
        if ind == -1:
            return nums.reverse()
        ind2=-1
        for i in range(n-1,ind,-1):
            if nums[i]>nums[ind]:
                ind2=i
                break
        nums[ind],nums[ind2]=nums[ind2],nums[ind]
        nums[ind+1:] = reversed(nums[ind+1:])
        return nums

                