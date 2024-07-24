class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preq[crs].append(pre)
        visit = set()
        cycle = set()
        res = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in preq[crs]:
                if not dfs(pre):
                    return False       
            visit.add(crs)
            cycle.remove(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res


            