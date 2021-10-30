class Solution {
public:
    int maxRepeating(string s, string w) {
      int n = s.length(), ans =0;
        for(int i= 0, j=0, k=0, l=0; i<n; i++,j=0, k=0, l=0){
            while(i+j<n && s[i+j]==w[l]){
                
                j++;l++;
                if(l==w.length()) l=0, k++;
            }
            ans = max(ans, k);
        }
        return ans;
    }
};