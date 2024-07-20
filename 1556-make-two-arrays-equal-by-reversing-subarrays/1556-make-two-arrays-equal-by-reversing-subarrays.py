class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = collections.defaultdict(int)
        for i in range(len(target)):
            count[target[i]] = count.get(target[i],0)+1
            count[arr[i]]-=1
        
        for k in count.values():
            if k:
                return False
        return True
        