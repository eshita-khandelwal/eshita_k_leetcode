class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        vector<string> ans;
        unordered_map<string,multiset<string>> hash;
        for(int i=0;i<tickets.size();i++)
        {
            hash[tickets[i][0]].insert(tickets[i][1]);
        }
        
       // ans.push_back("JFK");
        //ans.push_back(hash[ans.back()][])
        
        stack<string> mystack;
        mystack.push("JFK");
        while(!mystack.empty())
        {
            string src=mystack.top();
            if(hash[src].size()==0)
            {
                ans.push_back(src);
                mystack.pop();
            }
            else
            {
                auto des=hash[src].begin();
                mystack.push(*des);
                hash[src].erase(des);
            }
        }
        reverse(ans.begin(),ans.end());
        return ans;
        
    }
};