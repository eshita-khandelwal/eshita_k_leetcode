class Solution {
public:
    int calculate(string s) {
        stack<int> s1;
        if(s.size()==0)
            return 0;
        
        int curr=0;
        char op='+';
        
        for(int i=0;i<s.size();i++)
        {
            
            if(int(s[i])-'0' >=0 && int(s[i])-'0'<=9){
                //cout<<int(s[i])-'0' << "  ";
                curr=(curr*10)+(int(s[i])-'0');
               
            }
            
            if(!isdigit(s[i]) && !iswspace(s[i]) || i==s.size()-1)
            {
                if(op=='-')
                    s1.push(-curr);
                else if(op=='+'){
                    s1.push(curr);}
                else if(op=='*')
                {
                    int top=s1.top();
                    s1.pop();
                    s1.push(top*curr);
                }
                else if(op=='/')
                {
                    int top=s1.top();
                    s1.pop();
                    s1.push(top/curr);
                }
                
                op=s[i];
                curr=0;
                
            }
        }
         int result = 0;
        while (s1.size() != 0) {
            result += s1.top();
            s1.pop();
        }
        return result;
        
    }
};