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
    vector<int> res;
    void printright(TreeNode* root,int level)
    {
        if(root==NULL)
            return;
        
        if(res.size()<level)res.push_back(root->val);
        if(root->right)
         printright(root->right,level+1);
        if(root->left)
            printright(root->left,level+1);
       
           
        
    }
    vector<int> rightSideView(TreeNode* root) {
        printright(root,1);
        return res;
    }
};