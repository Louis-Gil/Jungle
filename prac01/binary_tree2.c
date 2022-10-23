#include "binary_tree2.h"
// malloc 반환값 체크 - 8, 14, 21line tree가 null이라면 처리, 반환
// 포인터 역참조 전에 NULL체크 - 28, 31등 cur이 null일수있음
//트리
Node tree = NULL;

Node makeRoot(DATA data){
    tree = (struct _Node*)malloc(sizeof(struct _Node));
    tree->data = data;
    tree->lchild = tree->rchild = NULL;
    return tree;
}
Node makeLeftChild(Node cur, DATA data){
    struct _Node* newnode = (struct _Node*)malloc(sizeof(struct _Node));
    newnode->data = data;
    newnode->lchild = tree->rchild = NULL;
    cur->lchild = newnode;
    return newnode;
}
Node makeRightChild(Node cur, DATA data){
    struct _Node* newnode = (struct _Node*)malloc(sizeof(struct _Node));
    newnode -> data = data;
    newnode -> lchild = tree -> rchild = NULL;
    cur -> rchild = newnode;
    return newnode;
}
DATA getCurData(Node cur){
    return cur -> data;
}
Node getLeftChild(Node cur){
    return cur -> lchild;
}
DATA getLeftChildData(Node cur){
    return cur -> lchild -> data;
}
Node getRightchild(Node cur){
    return cur -> rchild;
}
DATA getRightchildData(Node cur){
    return cur -> rchild -> data;
}
int isTreeEmpty(Node root){
    if(root == NULL)
        return 1;
    else
        return 0;
}