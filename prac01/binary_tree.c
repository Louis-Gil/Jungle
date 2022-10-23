#include "binary_tree.h"
//배열의 크기에 대한 예외가 생략되어있음
//트리
#define NODE_MAXCOUNT 100
DATA tree[NODE_MAXCOUNT] = {0}; //0값을 empty표시

Node makeRoot(DATA data){
    tree[1] = data;
    return 1;
}
Node makeLeftChild(Node cur, DATA data){
    tree[cur*2] = data;
    return cur *2;
}
Node makeRightChild(Node cur, DATA data){
    tree[cur*2 + 1] = data;
    return cur *2 +1;
}
DATA getCurData(Node cur){
    return tree[cur];
}
Node getLeftChild(Node cur){
    return cur*2;
}
DATA getLeftChildData(Node cur){
    return tree[cur*2];
}
Node getRightchild(Node cur){
    return cur*2 +1;
}
DATA getRightchildData(Node cur){
    return tree[cur*2 +1];
}
int isTreeEmpty(Node root){
    if(tree[root]==0)
        return 1;
    else
        return 0;
}