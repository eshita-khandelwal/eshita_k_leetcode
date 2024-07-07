class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #get the maximum occuring character, subtract from the length of the window and then see if is less than value of k. if greater than k then we need to move the left pointer. use a hash map 
        l=0
        res=0#length of the longest string with replacements done
        count = {}#to store count of the characters
        for r in range(len(s)):
            count[s[r]] = 1+count.get(s[r],0)
            while (r-l+1) - max(count.values())>k:
                count[s[l]]-=1
                l+=1
            res = max(res,(r-l+1))
        return res