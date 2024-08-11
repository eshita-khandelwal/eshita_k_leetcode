class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        card = {}
        for i in range(len(hand)):
            card[hand[i]] = 1 + card.get(hand[i],0)
        card = sorted(card.items(),key = lambda x:x[0])
        dic = {key: value for key, value in card}
        g = groupSize
        group = len(hand)//groupSize
        
        while group>0:
            g = groupSize
            prev = -1
            for k,v in dic.items():
                if v==0:
                    continue
                if g==0:
                    break
                if prev==-1:
                    dic[k]-=1
                    g-=1
                    prev = k
                elif prev == k-1:
                    g-=1
                    dic[k]-=1
                    prev = k
                else:
                    break
            group-=1
        return True if sum(dic.values())==0 else False

       

                
                
