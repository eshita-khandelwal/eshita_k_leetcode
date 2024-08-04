class Solution:
    def splitNum(self, num: int) -> int:
        l = []
        while num>0:
            l.append(num%10)
            num=num//10
        
        l.sort()
        x = len(l)//2
        num1=""
        num2=""
        i = 0
        while i<len(l):
            num1+=str(l[i])
            i+=1
            if i<len(l):
                num2+=str(l[i])
            i+=1
        if num1=="": 
            return int(num2)
        if num2=="":
            return int(num1)
        return int(num1)+int(num2)
        



