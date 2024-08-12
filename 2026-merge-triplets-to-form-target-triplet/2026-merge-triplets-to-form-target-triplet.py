class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # for i,j,k in triplets:
        #     if i==target[0] and j==target[1] and k==target[2]:
        #         return True
        
        # maxi = maxj = maxk = 0
        # max1 = max(target[0],target[1],target[2])
        # for i in range(len(triplets)):
        #     if max(triplets[i][0],triplets[i][1],triplets[i][2])>max1:
        #         continue
        #     maxi=max(maxi,triplets[i][0])
        #     maxj=max(maxj,triplets[i][1])
        #     maxk=max(maxk,triplets[i][2])
        #     if [maxi,maxj,maxk]==target:
        #         return True
        
        # return False
        a,b,c = 0,0,0
        for i in range(len(triplets)):
            if(triplets[i][0]<=target[0] and triplets[i][1]<=target[1] and triplets[i][2]<=target[2]):
                a = max(a,triplets[i][0])
                b = max(b,triplets[i][1])
                c = max(c,triplets[i][2])
            if a==target[0] and b==target[1] and c==target[2]:
                return True
        return False
                