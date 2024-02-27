#include "same_tree_header.h"

//the method below creates a node, sets the value of the node to the value passed, and sets the left and right children to null.
 struct TreeNode* treeNodeCreation (int value) {
        struct TreeNode *node = malloc(sizeof(struct TreeNode));
        /*creates pointer variable called node that points to the struct TreeNode. 
        This variable is then assigned the memory location of the first byte in the heap created by malloc. 
        Malloc also allocates memory in the heap in reference to the size of the struct TreeNode.*/
        node->left = NULL; //null indicates that there are no children
        node->right = NULL;
        node->val = value; 

        return node;
    }

    //this is also practice for traversal even though it is not necessary for this problem

// void preOrderTraversal(struct TreeNode* root) {
//     if (root!= NULL) {
//         preOrderTraversal(root->left);
//         preOrderTraversal(root->right);
//     }
// }


bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    
    /*struct TreeNode *n1 = treeNodeCreation(p->val);
    struct TreeNode *n2 = treeNodeCreation(q->val);

    We are creating two nodes using the treeNodeCreation method and passing by value the value of val in the p and q structs

    The above initializations are not required for this program but I just wanted to practice creating a node as all this has been pretty abstract. */

    if (p == NULL && q == NULL) {//base case
        return true;
    }

    if (p == NULL || q == NULL) {//edge case
        return false;
    }

    if (p->val != q->val) {//check current value
        return false;
    }

    return isSameTree(p->left, q->left) && isSameTree(p->right, q->right); //recursive call
}