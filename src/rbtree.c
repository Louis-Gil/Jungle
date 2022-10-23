#include "rbtree.h"
#include <stdlib.h>
//#include <stdio.h>

rbtree *new_rbtree(void) {
  // TODO: initialize struct if needed
  rbtree *p = (rbtree *)calloc(1, sizeof(rbtree));
  node_t *NIL = (node_t *)calloc(1, sizeof(node_t));
  NIL -> color = RBTREE_BLACK;
  NIL -> parent = NIL;
  p -> root = NIL;
  p -> nil = NIL;
  return p;
}

void delete_rbtree(rbtree *t) {
  // TODO: reclaim the tree nodes's memory
  free(t);
}

// node_t *rbtree_insert(rbtree *t, const key_t key) {
//   // TODO: implement insert
//   return t->root;
// }

node_t *rbtree_insert(rbtree *t, const key_t key) {
  // TODO: implement insert
  struct node_t * Nil = t->nil;
  struct node_t * Cur = t->root;
  struct node_t * parent = Cur;
  
  while(Cur != Nil)
  {
    parent = Cur;
    if(Cur->key == key){
      // printf("중복된 숫자는 넣을 수 없습니다.\n");
      return Cur; //*t? &t?
    }
    else if(Cur->key > key)
      Cur = Cur->left;
    else
      Cur = Cur->left;
  }

  node_t *new_Node = (node_t *)calloc(1, sizeof(node_t));
  new_Node->color = RBTREE_RED;
  new_Node->key = key;
  new_Node->parent = parent;
  new_Node->left = Nil;
  new_Node->right = Nil;

  if(parent != Nil){
    if (parent->key > key)
      parent->left = new_Node;
    else
      parent->right = new_Node;
  }
  else
    t->root = new_Node;

  return new_Node;
}

node_t *rbtree_find(const rbtree *t, const key_t key) {
  // TODO: implement find
  return t->root;
}

node_t *rbtree_min(const rbtree *t) {
  // TODO: implement find
  return t->root;
}

node_t *rbtree_max(const rbtree *t) {
  // TODO: implement find
  return t->root;
}

int rbtree_erase(rbtree *t, node_t *p) {
  // TODO: implement erase
  return 0;
}

int rbtree_to_array(const rbtree *t, key_t *arr, const size_t n) {
  // TODO: implement to_array
  return 0;
}
