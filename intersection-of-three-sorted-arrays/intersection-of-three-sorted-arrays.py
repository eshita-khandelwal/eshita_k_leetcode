class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        d = {}
        for i,val in enumerate(arr1):
            if val not in d:
                d[val]=1
            else:
                d[val]+=1
        for i,val in enumerate(arr2):
            if val not in d:
                continue
            else:
                d[val]+=1
        for i,val in enumerate(arr3):
            if val not in d:
                continue
            else:
                d[val]+=1
        ans = []
        for i in d:
            if d[i] == 3:
                ans.append(i)
        # ans.sort()
        return ans
        
            