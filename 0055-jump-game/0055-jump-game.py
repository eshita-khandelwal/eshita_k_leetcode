class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1 #our goal post, idea is to move the goal post to the start
        for i in range(len(nums)-1,-1,-1): #traverse the array in reverse order
            if nums[i] + i >=goal:
                goal = i

        return True if goal==0 else False