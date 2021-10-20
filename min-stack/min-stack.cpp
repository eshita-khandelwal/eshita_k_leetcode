class MinStack {
public:
    /** initialize your data structure here. */
    struct node
    {
        int val;
        int min1;
        node *next;
        node *prev;
    };
   // int min=INT_MAX;
    
      node *head=new node();
    node *tail=new node();
   
    MinStack() {
      head->next=tail;
    tail->prev=head;
    head->prev=NULL;
    tail->next=NULL;
        head->min1=INT_MAX;
        tail->min1=INT_MAX;
    }
    
    void push(int val) {
       node *newnode=new node();
        newnode->val=val;
        newnode->next=head->next;
            head->next->prev=newnode;
        head->next=newnode;
        newnode->prev=head;
        if(newnode->val<newnode->next->min1){
            newnode->min1=newnode->val;
        }
        else
            newnode->min1=newnode->next->min1;
        
    }
    
    void pop() {
        if(head->next!=tail){
        head->next=head->next->next;
        head->next->prev=head;
            
        }
    }
    
    int top() {
        if(head->next!=tail)
       return head->next->val; 
        
        return NULL;
    }
    
    int getMin() {
     return head->next->min1;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */