/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *slow=head;
        ListNode *fast=head;
        
        while(slow && fast && fast->next)
        {
            fast=fast->next->next;
            slow=slow->next;
            if(fast==slow)
                return true;
        }
        return false;
        
        // unordered_map<ListNode *,int> a;
        // ListNode *f=head;
        // while(f!=NULL)
        // {
        //     a[f]++;
        //     if(a[f]>1)
        //         return true;
        //     f=f->next;
        // }
        // return false;
    }
};