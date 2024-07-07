class TimeMap:

    def __init__(self):
        self.dict={} #key:[[val,timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key]=[]
        self.dict[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.dict.get(key,[])
        l,r=0,len(values)-1
        res=''
        while l<=r:
            mid = (l+r)//2
            if values[mid][1]<=timestamp:
                res=values[mid][0]
                l = mid+1
            else:
                r = mid-1
        
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)