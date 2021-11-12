class Solution {
public:
    string reformatDate(string date) {
        
        size_t x,y;
         x=date.find(' ');
        string day=date.substr(0,x);
        y=date.find(" ",x+1);
        string month=date.substr(x+1,3);
        string year=date.substr(y+1);
        
        string result;
        result+=year+"-";
        
        string months[12]={"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
        for(int i=0;i<12;i++)
        {
            if(months[i]==month)
            {
                if(i+1<10)
                    result+=to_string(0)+to_string(i+1)+"-";
                    else
                result+=to_string(i+1)+"-";
            }
        }
        string d;
       for(int i=0;i<x;i++)
       {
           if(isdigit(day[i]))
               d+=day[i];
               
       }
        if(d.size()==1)
        d.insert(d.begin(),'0');
        result+=d;
        return result;
    }
};