class Solution {
public:
    int compress(vector<char>& chars) {
       
        string ans;
        int c=1,i=0;
        int flag=0;
        int pos=-1;
        //char s;
        for(i=0;i<chars.size()-1;i++)
        {
            if(chars[i]==chars[i+1])
            {
                if(flag==0)
                {
                    pos=i;
                    //ans+=chars[i];
                    flag=1;
                    //c++;
                }
                c++;
            }
            else
            {
                if(pos!=-1)
                ans+=chars[pos];
                else
                    ans+=chars[i];
//                 if(ans.size()==0 || ans[ans.size()-1]!=chars[i]){
                    
//                     ans+=chars[i];
//                 }
                if(c>1)
                {
                ans+=to_string(c);
                c=1;
                flag=0;
                    pos=-1;
                }
            }
        }
        if(pos!=-1)
                ans+=chars[pos];
                else
                    ans+=chars[i];
                if(c>1){
                ans+=to_string(c);
                c=1;
                flag=0;
                }
        
        for(int j=0;j<ans.size();j++)
        {
            chars[j]=ans[j];
        }
        return ans.size();
    }
};