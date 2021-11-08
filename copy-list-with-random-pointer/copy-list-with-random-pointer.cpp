/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*,Node*> map;
        
        Node *temp=head;
        while(temp!=NULL)
        {
            Node *newnode=new Node(temp->val);
            // newnode->next=NULL;
            // newnode->random=NULL;
                
            map[temp]=newnode;
            temp=temp->next;
        }
        
        temp=head;
        while(temp!=NULL)
        {
            map[temp]->random=map[temp->random];
            map[temp]->next=map[temp->next];
            temp=temp->next;
        }
        
        
        return map[head];
    }
};