class Solution {
public:
    static bool comp(pair<string,int> &a,pair<string,int> &b)
    {
        
        if(a.second!=b.second)
        return a.second>b.second;
        return a.first<b.first;
        
    }
 
    vector<string> topKFrequent(vector<string>& words, int k) {
        
        map<string,int> map;
        sort(words.begin(),words.end());
        
        for(int i=0;i<words.size();i++)
        {
           // cout<<words[i]<<"  ";
            map[words[i]]++;
        }
       vector<pair<string,int>> count;
       // vector<pair<int,vector<string>>> count1;
        vector<string> f;
        for(auto x:map)
        {
            count.push_back(x);
          
        }
      
        sort(count.begin(),count.end(),comp);
     
         for(int i=0;i<k;i++)
        {
             cout<<count[i].second<<"  ";
            f.push_back(count[i].first);
            
        }
        
   
        
     
       
      
        return f;
    }
};