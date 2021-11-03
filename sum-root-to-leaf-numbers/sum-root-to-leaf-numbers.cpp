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
    int sum(TreeNode *root,int num)
    {
         return (root->left==root->right ? num*10+root->val : 
                 (root->left? sum(root->left,num*10+root->val) : 0)+(root->right ? sum(root->right,num*10+root->val) : 0));
    }
    int sumNumbers(TreeNode* root) {
        
       int x=sum(root,0);
        return x;
    }
};