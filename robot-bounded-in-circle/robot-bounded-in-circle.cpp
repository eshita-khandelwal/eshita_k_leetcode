class Solution {
public:
    bool isRobotBounded(string instructions) {
        
        int dx=0;//direction of x
        int dy=1; // direction of y(initially facing up)
        
        int x=0,y=0;
        for(int i=0;i<instructions.size();i++)
        {
            if(instructions[i]=='G')
            {
                x=dx+x;
                y=dy+y;
            }
            else if(instructions[i]=='L')
            {
                int m=dx;
                dx=-1*dy;
                dy=m;
            }
            else
            {
                int m=dy;
                dy=-1*dx;
                dx=m;
            }
        }
        
        return  (x==y && x==0) || (dx!=0 || dy!=1);
            
    }
};