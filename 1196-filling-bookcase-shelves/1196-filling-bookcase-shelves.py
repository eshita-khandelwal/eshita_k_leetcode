class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        #knapsack category
        cache = {}
        def helper(i): #recurssive function
            if i == len(books):
                return 0 #base case
            if i in cache:
                return cache[i]
            maxheight=0
            cache[i]=float("inf")
            cur_width = shelfWidth #we are starting at a new shelf everytime so the capacity is full
            for j in range(i,len(books)):
                width, height= books[j]
                if cur_width<width:
                    break
                cur_width-=width
                maxheight = max(maxheight,height)
                cache[i] = min(cache[i],helper(j+1)+maxheight)
            return cache[i]
        return helper(0)


