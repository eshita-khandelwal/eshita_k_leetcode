class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        #link : https://www.youtube.com/watch?v=BueoreUIkcE
        # the idea is to use sliding window . max window size can be total number of ones in the entire list. if the window size becomes greater than total no of ones then we do l+=1
        #also keep track of max ones found in each window size and then toal swaps required will be total of ones - max of ones found in a window 

        n = len(nums)
        l = 0
        total_ones = nums.count(1)
        maxones = windowones = 0
        for r in range(2*n):#doing this because of circular array.
            if nums[r%n]:
                windowones+=1
            if r-l+1>total_ones:
                windowones-=nums[l%n]
                l+=1
            maxones= max(maxones,windowones)
        return total_ones-maxones
