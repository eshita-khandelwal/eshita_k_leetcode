class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        
        int i=0,j=0,count=0;
        int hash[256]={0};
        int max1=INT_MIN;
        while(j<s.size())
        {
            hash[s[j]]++;
            if(hash[s[j]]==1)count++;
           
                while(count>2)
                {
                    hash[s[i]]--;
                    if(hash[s[i]]==0)count--;
                    i++;
                }
            
            max1=max(max1,j-i+1);
            j++;
            
        }
        
        return max1;
    }
};