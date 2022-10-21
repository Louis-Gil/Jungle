#ifndef _BINARYTREE_H_
#define _BINARYTREE_H_

#include<stdio.h>
#include<stdlib.h>
#include<memory.h>

typedef char DATA;
typedef struct _Node{
    DATA data;
    struct _Node* lchild;
    struct _Node* rchild;
}*Node;
Node makeRoot(DATA data);
Node makeLeftChild(Node cur, DATA data);
Node makeRightChild(Node cur, DATA data);
DATA getCurData(Node cur);
Node getLeftChild(Node cur);
DATA getLeftChildData(Node cur);
Node getRightchild(Node cur);
DATA getRightchildData(Node cur);
int isTreeEmpty(Node root);

#endif //binary_tree.h