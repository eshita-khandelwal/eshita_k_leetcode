class Solution {
public:
    bool validWordSquare(vector<string>& words) {
     
        // vector<int> l;
        // for(int i=0;i<words.size();i++)
        //     l.push_back(words.size());
        // for(int i=0;i<l.size()-1;i++)
        // {
        //     if(l[i]==l[i+1]){}
        //     else
        //         return false;
        // }
        // if(l[l.size()-1]!=l[l.size()-1])
        //     return false;
        for(int i=0;i<words.size();i++)
        {
            string f;
            for(int j=0;j<min(words[i].size(),words.size());j++)
            {
                f+=words[j][i];
            }
            //cout<<f<<endl;
            if(f==words[i])
                continue;
            else
                return false;
        }
        return true;
    }
};