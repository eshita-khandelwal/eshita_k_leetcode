/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> s1,s2;
        int sum=0,c=0;
        while(l1!=NULL){
            s1.push(l1->val);
            l1=l1->next;
        }
        while(l2!=NULL){
            s2.push(l2->val);
            l2=l2->next;
        }
        ListNode *temp3=new ListNode(0);
        while(!s1.empty() && !s2.empty())
        {
            int sum=s1.top()+s2.top()+c;
             s1.pop();
            s2.pop();
            if(sum>9){
                int x=sum;
                sum=sum%10;
                c=x/10;
            }
            else
            {
                c=0;
            }
            ListNode *temp=new ListNode(sum);
            ListNode *l3=temp3;
            while(l3->next!=NULL)
                l3=l3->next;
            l3->next=temp;    
        }
         while(!s2.empty())
        {
            int sum=s2.top()+c;
            if(sum>9){
                int x=sum;
                sum=sum%10;
                c=x/10;
            }
            else
            {
                c=0;
            }
              ListNode *temp=new ListNode(sum);
              ListNode *l3=temp3;
            while(l3->next!=NULL)
                l3=l3->next;
            l3->next=temp;
            s2.pop();        
        }
         while(!s1.empty())
        {
            int sum=s1.top()+c;
            if(sum>9){
                int x=sum;
                sum=sum%10;
                c=x/10;
            }
            else
            {
                c=0;
            }
              ListNode *temp=new ListNode(sum);
              ListNode *l3=temp3;
            while(l3->next!=NULL)
                l3=l3->next;
            l3->next=temp;
            s1.pop();      
        }
        if(c>0)
        {
              ListNode *temp=new ListNode(c);
             ListNode *l3=temp3;
             while(l3->next!=NULL)
                l3=l3->next;
            l3->next=temp;
        }
        
        ListNode *curr=temp3->next;  //I do not want to consider 0 that i have put in the beginning of temp3 list.
        ListNode *prev=NULL;
        
        while(curr!=NULL)
        {
            ListNode  *next=curr->next; 
            curr->next=prev;
            prev=curr;
            curr=next;
        }
        temp3=prev;
        return temp3;
        
    }
};