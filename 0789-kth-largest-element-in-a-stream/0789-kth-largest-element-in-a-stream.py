class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap,self.k = nums,k #member variables
        heapq.heapify(self.minheap) #inbuild heap python
        while len(self.minheap)>k:
            heapq.heappop(self.minheap)
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap,val)
        if len(self.minheap)>self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)