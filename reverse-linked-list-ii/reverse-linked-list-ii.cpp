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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        
        if(head==NULL || head->next==NULL || left==right)
            return head;
        int cnt=0;
        ListNode *temp=head;
        ListNode *prev=NULL;
        while(temp!=NULL)
        {
            cnt++;
            if(cnt==left)
                break;
                prev=temp;
                temp=temp->next;
        }
        
        ListNode *s=temp;
        // cnt=0;
        temp=temp->next;
        while(temp!=NULL)
        {
           cnt++;
            if(cnt==right)
                break;
            temp=temp->next;
            
        }
        ListNode *e=temp->next;
        temp=s;
        //cout<<temp->val<<"   "<<e->val;
        ListNode *next;
        ListNode *prev1=prev;
        while(temp!=e)
        {
            next=temp->next;
            //cout<<next->val<<"  ";
            if(temp==s){}
            else
            temp->next=prev;
            prev=temp;
            temp=next;
        }
        if(prev1!=NULL)
        prev1->next=prev;
        else
            head=prev;
        s->next=temp;
        
        return head;
    }
};