class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = {}
        for i in range(len(target)):
            count[target[i]] = count.get(target[i],0)+1
        
        for i in range(len(arr)):
            if arr[i] in count and count[arr[i]]>0:
                count[arr[i]]-=1
            else:
                return False
       
        return True
        