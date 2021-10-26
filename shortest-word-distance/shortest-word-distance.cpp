class Solution {
public:
    int shortestDistance(vector<string>& w, string word1, string word2) {
        
        int d=0;
        
        int d1=-1,d2=-1;
        int min1=INT_MAX;
        for(int i=0;i<w.size();i++)
        {
            if(w[i]==word1){
               
                 d1=i;   
            }
              if(w[i]==word2){
                d2=i;}
            
            if(d1!=-1 && d2!=-1)
            {
                if(abs(d1-d2)<min1)
                    min1=abs(d1-d2);
            }
            
        }
        
        return min1;
        
        
    }
};