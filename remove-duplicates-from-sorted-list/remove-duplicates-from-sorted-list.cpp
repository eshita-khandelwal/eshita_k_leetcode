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
    ListNode* deleteDuplicates(ListNode* head) {
        if(head==NULL || head->next==NULL)
            return head;
     
       // ListNode *prev=head;
         ListNode *temp=head;
        while(temp!=NULL)
        {
            ListNode *next1=temp->next;
            if(next1!=NULL && temp->val==next1->val)
            {
                temp->next=next1->next;
            }
            else
            temp=temp->next;
            
        }
       
       
        
        return head;
    }
};