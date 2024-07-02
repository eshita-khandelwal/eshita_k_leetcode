class Solution(object):
    def dailyTemperatures(self, temps):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res=[0]*len(temps)
        stack=[]#pair(temp,ind)
        for ind,temp in enumerate(temps):
            while stack and temp>stack[-1][0]:
                t,i = stack.pop()
                res[i] = (ind-i)
            stack.append([temp,ind])
        return res