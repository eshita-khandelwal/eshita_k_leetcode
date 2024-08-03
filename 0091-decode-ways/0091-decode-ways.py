class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}
       #if the string starts with 0 we would do dp[i]=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]    
            if (i+1<len(s) and (s[i]=='1' or s[i]=='2' and s[i+1] in "0123456")): #this ensures that string starting from 0 will not be considered like 06. only considers if example s[0]=1 and s[2]=3 
                dp[i]+=dp[i+2]
        print(dp)
        return dp[0] 