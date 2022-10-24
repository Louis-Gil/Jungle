#include "rbtree.h"
#include <stdio.h>

int main(int argc, char *argv[]) {
    rbtree *T = new_rbtree();
    rbtree_insert(T, 1000);
    rbtree_insert(T, 2000);
    rbtree_insert(T, 1500);
    // rbtree_insert(T, 2500);
    // rbtree_insert(T, 500);
    printf("%d %d\n", T->root->key, T->root->color);
    printf("%d %d\n", T->root->left->key, T->root->left->color);
    printf("%d %d\n", T->root->right->key, T->root->right->color);
    // printf("%d\n", T->root->left->left->key);
    // printf("%d\n", T->root->right->right->key);
}