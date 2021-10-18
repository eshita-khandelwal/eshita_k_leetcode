class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        map<int, int> mp; //map is sorting the values entered in sorted order.
         for(int i=0; i< intervals.size(); i++) {
        mp[intervals[i][0]] ++;
        mp[intervals[i][1]] --;
    }
    
    int cnt = 0, maxCnt = 0;
    for(auto it = mp.begin(); it != mp.end(); it++) {
       // cout<<it->first<<"    "<<it->second<<"    "<<cnt<<endl;
        cnt += it->second;
        maxCnt = max( cnt, maxCnt);
    }
    
    return maxCnt;
    }
};