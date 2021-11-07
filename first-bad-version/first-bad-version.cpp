// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
       
        int left=1;
        int right=n;
        if(left==right)
            return left;
        int mid;
        while(left<=right)
        {
         mid=left+(right-left)/2;
            
            if(isBadVersion(left))
                return left;
            
            else if(isBadVersion(mid))
                right=mid;
            else if(isBadVersion(mid)==false)
                left=mid+1;
            
        }
        return mid;
    }
};