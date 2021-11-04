/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> x;
    void sum(TreeNode *root,bool isleft)
    {
        if(root->left==root->right){
            if(isleft)
            x.push_back(root->val);
            return ;
        }
          if(root->left)
              sum(root->left,true);
        if(root->right)
            sum(root->right,false);
    }
    int sumOfLeftLeaves(TreeNode* root) {
       int s=0;
        if(root==NULL)
            return 0;
    // if(root->left==NULL)
    //     return 0;
        sum(root,false);
        
        for(int i=0;i<x.size();i++){
            cout<<x[i]<<"   ";
            s+=x[i];}
        
        
        return s;
    }
};