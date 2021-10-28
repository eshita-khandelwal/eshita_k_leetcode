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
    ListNode *reverse(ListNode *head)
    {
        if (head == NULL || head->next == NULL)
            return head;
 
        /* reverse the rest list and put
          the first element at the end */
        ListNode* rest = reverse(head->next);
        head->next->next = head;
 
        /* tricky step -- see the diagram */
        head->next = NULL;
 
        /* fix the head pointer */
        return rest;
        
    }
    ListNode* plusOne(ListNode* head) {
        
        int s=0,c=0;
        
        ListNode *head1=head;
        ListNode *headr=NULL;
        while(head1!=NULL)
        {
            ListNode *temp=new ListNode(head1->val);
            temp->next=NULL;
            if(headr==NULL)
                headr=temp;
            else
            {
               ListNode *t= headr;
                while(t->next!=NULL)
                    t=t->next;
                t->next=temp;
            }
            head1=head1->next;
        }
        
        headr=reverse(headr);
        
        head1=headr;
        int f=0;
   ListNode *prev=NULL;
        while(head1!=NULL)
        {
            cout<<head1->val<<endl;
            
            if(f==0)
            {
                if(head1->val+1>9)
                {
                   
                    c=(head1->val+1)/10;
                     head1->val=(head1->val+1)%10;
                }
                else
                {
                    head1->val=head1->val+1;
                }
                f=1;
            }
            
            else if(c>0)
            {
                if(head1->val+c>9){
                
                    c=(head1->val+c)/10;
                    head1->val=(head1->val+c)%10;
                }
                else{
                  head1->val=head1->val+c;
                c=0;}  
                
            }
            prev=head1;
            head1=head1->next;
            
            
        }
        
        if(c!=0)
        {
            ListNode *newn=new ListNode(c);
            newn->next=NULL;
            prev->next=newn;
        }
        
        headr=reverse(headr);
        return headr;
        
    }
};