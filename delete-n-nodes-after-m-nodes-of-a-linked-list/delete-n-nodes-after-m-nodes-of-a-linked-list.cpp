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
    ListNode* deleteNodes(ListNode* head, int m, int n) {
       
        ListNode *curr=head;
        ListNode *prev = curr;
        int cnt=0;
        while(curr!=NULL){
            cnt = 0;
        while(cnt<m && curr!=NULL)
        {
            prev=curr;
            curr=curr->next;
            cnt++;
            
        }
        ListNode *temp=curr;
        cnt=0;
        while(cnt<n && temp!=NULL)
        {
            temp=temp->next;
            cnt++;
        }
        
        if(prev!=NULL)
        {
            prev->next=temp;
        }
        
        curr=temp;
        }
        return head;
        
        

        
    }
};