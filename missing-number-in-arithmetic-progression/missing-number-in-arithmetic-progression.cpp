class Solution {
public:
    int missingNumber(vector<int>& arr) {
        int s=((arr.size()+1)*(arr[0]+arr[arr.size()-1]))/2;
        int s1=0;
        for(int i=0;i<arr.size();i++)
            s1+=arr[i];
        
        return s-s1;
    }
};