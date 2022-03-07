class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        
        int c[26]={0};
        
         int len=0;
         for(int i=0;i<chars.size();i++)
         {
             c[int(chars[i])-97]++;
         }
         
        for(int i=0;i<words.size();i++)
        {
            int f=0;
            int d[26]={0};
           for(int j=0;j<words[i].size();j++)
           {
               d[int(words[i][j])-97]++;
               if(d[int(words[i][j])-97]>c[int(words[i][j])-97])
               {
                   f=1;break;
               }
           }
           
            
            if(f==0)
                len+=words[i].size();
        }
        
        return len;
    }
};