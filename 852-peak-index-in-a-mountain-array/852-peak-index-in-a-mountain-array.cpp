class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        
        int p=-1;
        for(int i=1;i<arr.size()-1;i++)
        {
           // cout<<i<<endl;
            if(arr[i]>arr[i-1] && arr[i]>arr[i+1])
            {
                p=i;
                break;
            }
        }
       return p;
    }
};