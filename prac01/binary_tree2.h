#ifndef _BINARYTREE_H_
#define _BINARYTREE_H_

#include<stdio.h>
#include<stdlib.h>
#include<memory.h>

typedef char DATA;
typedef struct _Node{ 
//이러한 스트럭처가 _노드를 가르킴
//그거에 대한 타입이 노드
    DATA data;
    struct _Node* lchild;//(자기 자신을 가르키는 lchild)
    struct _Node* rchild;
}*Node; //그 구조체에 대한 포인트 타입을 노드라고 해야합니다

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