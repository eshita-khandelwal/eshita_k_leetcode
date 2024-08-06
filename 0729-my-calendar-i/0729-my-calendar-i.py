class MyCalendar:

    def __init__(self):
       self.mycal = [] 

    def book(self, start: int, end: int) -> bool:
        if len(self.mycal) ==0:
            self.mycal.append([start,end])
            return True
        else:
            for s,e in self.mycal:
                if (end<=e and end>s) or (start>=s and start<e):
                    return False 
                if s>start and e<end:
                    return False
            self.mycal.append([start,end])
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)