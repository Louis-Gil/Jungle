#include "rbtree.h"
#include <stdlib.h>

void delete_rbtree(rbtree *t);
void delete_rbtree_rep(node_t *NIL, node_t *p);
node_t *rbtree_insert(rbtree *t, const key_t key);
void struct_fix(rbtree *t, node_t *new_Node);
void rbtree_condition_case1(rbtree *t);
int rbtree_condition_case2(node_t* new_Node, node_t* parent, node_t *granpa, node_t * uncle);
void rbtree_condition_case3(node_t* new_Node, rbtree *t);
/*


*/

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
  node_t *NIL = t->nil;
  delete_rbtree_rep(NIL, t->root);
  free(t->nil);
  free(t);
}

void delete_rbtree_rep(node_t *NIL, node_t *p){
  while(p != NIL){
    // delete_rbtree_rep(p->left);
    // delete_rbtree_rep(p->right);
    free(p);
  }
}

node_t* rbtree_insert(rbtree *t, const key_t key) {
  // TODO: implement insert
  node_t * Nil = t->nil;
  node_t * p = t->root;
  node_t * parent = Nil;
  
  while(p != Nil)
  {
    parent = p;
    if(p->key > key) 
      p = p->left;
    else
      p = p->right;
  }

  node_t* new_Node = (node_t *)calloc(1, sizeof(node_t));
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
  else{
    t->root = new_Node;
  }

  struct_fix(t, new_Node);
  return t->root;
  // return new_Node;
}

void struct_fix(rbtree *t, node_t *new_Node){
  node_t *parent = new_Node->parent;
  while(1){
    rbtree_condition_case1(t); //헤드노드 검은색
    if (parent->color == RBTREE_BLACK)
      break;

    node_t *granpa = parent->parent;
    node_t *uncle;
    if (granpa->left == parent)
      uncle = granpa->right;
    else
      uncle = granpa->left;

    if (rbtree_condition_case2(new_Node, parent, granpa, uncle) == 1)
      continue;//삼촌이 빨간색일 경우 색 변경

    rbtree_condition_case3(new_Node, t);
    
  }
}
void rbtree_condition_case1(rbtree *t){
  if (t->root->color == RBTREE_RED)
    t->root->color = RBTREE_BLACK;
}
int rbtree_condition_case2(node_t* new_Node, node_t *parent, node_t *granpa, node_t * uncle){
  if (uncle->color == RBTREE_RED){
    parent->color = RBTREE_BLACK;
    uncle->color = RBTREE_BLACK;
    granpa->color = RBTREE_RED;

    new_Node->parent = granpa;
    new_Node = parent;
    return 1;
  }
  return 0;
}
void rbtree_condition_case3(node_t* new_Node, rbtree *t){
  node_t *parent = new_Node->parent;
  node_t *granpa = parent->parent;
  node_t *NIL = t->nil;
  if (granpa->right==parent && parent->left == new_Node){
    granpa->right = new_Node;
    new_Node->right = parent;
    new_Node->parent = granpa;
    parent->parent = new_Node;
    parent->left = NIL;
  } //오른쪽으로 꺽은선 펴주기
  if (granpa->left==parent && parent->right == new_Node){
    granpa->left = new_Node;
    new_Node->left = parent;
    new_Node->parent = granpa;
    parent->parent = new_Node;
    parent->left = NIL;
  } //왼쪽으로 꺽은선 펴주기

  if (granpa->right == parent && parent->right == new_Node){
    granpa->right = parent->left;
    parent->left = granpa;     
  } //오른쪽으로 펴진선 정렬
  if (granpa->left == parent && parent->left == new_Node){
    granpa->left = parent->right;
    parent->right = granpa;
  } //왼쪽으로 펴진선 정렬

  if(granpa->parent == NIL){
    t->root = parent;
    parent->parent = t->root;
    granpa->parent = parent;
  }
  else{
    node_t* biggranpa = granpa->parent;
    if (biggranpa->left == granpa){
      biggranpa->left = parent;
      parent->parent = biggranpa;
    }
    else{
      biggranpa->right = parent;
      parent->parent = biggranpa;
    }
  }
  granpa->color = RBTREE_RED;
  parent->color = RBTREE_BLACK;   
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
