class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        maxArea=0
        minHeight=0
        while i<j:
            minHeight = min(height[i],height[j])
            maxArea = max(minHeight*(j-i),maxArea)
            if height[i]>=height[j]:
                j-=1
            else:
                i+=1
        
        return maxArea
