#include <stdio.h>
#include <stdlib.h>

typedef char data;
typedef struct _Node{
    char key;
    struct _Node* left;
    struct _Node* right;
} Node; 

Node* searchBST(Node* root, char x){
    Node* p = root;
    while(p != NULL){
        if (p->key == x)
            return p;
        else if (p->key < x)
            p = p->right;
        else
            p = p->left;
    }
    return NULL;
}

Node* insertBST(Node* root, char x){
    Node* p = root;
    Node* parent = NULL;// 한바퀴도 못돌경우
    while(p != NULL){
        parent = p;
        if (p->key == x){
            printf("같은 키가 있습니다.\n");
            return p;
        }
        else if (p->key < x)
            p = p->right;
        else
            p = p->left;
    }
    //새 노드 할당
    Node *newNode = (Node*)malloc(sizeof(Node));
    //실전에는 노트가 실패할 경우 필요
    newNode->key = x;
    newNode->left = newNode->right = NULL;

    //parent의 자식으로 새 노드 붙이기
    if (parent != NULL){
        if(parent->key < newNode->key)
            parent->right = newNode;
        else
            parent->left = newNode;
    }
    return newNode;
}

Node* deleteBST(Node* root, char x){
    Node* p = root;
    Node* parent = NULL;
    while((p != NULL) && (p->key != x)){
        parent = p;
        if (p->key < x)
            p = p->right;
        else
            p = p->left;
    }
    if (p == NULL){
        printf("찾는 노드가 없습니다.\n");
        return root;
    }
    //루트의 키가 x와 같아서 바로 빠진경우
    if (p->left == NULL && p->right == NULL) { //차수가 0
        if (parent == NULL)
            root = NULL;
        else{
            if (parent -> left == p)
                parent->left = NULL;
            else
                parent->right = NULL;
        }
    }
    else if(p->left == NULL || p->right ==NULL){ //차수가 1
        Node *child = (p->left != NULL) ? p->left : p->right;
        if(parent == NULL)
            root =child;
        else{
            if(parent -> left == p)
                parent -> left = child;
            else
                parent -> right = child; 
        }
    }
    else {//차수가 2
        Node* succ_parent = p;
        Node* succ = p->right;
        while(succ->left != NULL){
            succ_parent = succ;
            succ = succ->left;
        }
        p->key = succ -> key;
        if(succ_parent -> left == succ)//succ자식이 없는 경우
            succ_parent -> left = succ->right;
        else
            succ_parent -> right = succ -> right;
        p = succ;
    }
    
    free(p);
    return root;
}

void inorder(Node* root){
    if(root == NULL)
        return;
    inorder(root->left);
    printf("%c", root->key);
    inorder(root->right);
}

int main(){
    Node *root =insertBST(NULL, 'D');
    insertBST(root, 'I');
    insertBST(root, 'F');
    insertBST(root, 'A');
    insertBST(root, 'G');
    insertBST(root, 'C');
    inorder(root); printf("\n");
    root = deleteBST(root, 'C');
    inorder(root); printf("\n");
    return 0;
}