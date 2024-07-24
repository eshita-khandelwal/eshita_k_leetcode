class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preq[crs].append(pre)
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if preq[crs]==[]:
                return True
            visit.add(crs)
            for pre in preq[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            preq[crs]=[]
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
            
