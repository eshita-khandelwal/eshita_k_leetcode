class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        dict1 = {}# to store frequency of all word in words 
        for i in words:
            dict1[i]=dict1.get(i,0)+1
        
        word_len = len(words[0])#length of one word
        windowlen = len(words)*word_len
        i=0
        res=[]
        for i in range(len(s)-windowlen +1):
            j=i
            dict2={}
            while j<i+windowlen:
                w = s[j:j+word_len]
                if w not in dict1:
                    break
                dict2[w]=dict2.get(w,0)+1
                if dict2[w]>dict1[w]:
                    break
                j+=word_len
            if j==i+windowlen:
                res.append(i)
        
        return res

