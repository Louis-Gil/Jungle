#include "rbtree.h"
#include <stdlib.h>

void delete_rbtree(rbtree *t);
void delete_rbtree_rep(node_t *NIL, node_t *p);
node_t *rbtree_insert(rbtree *t, const key_t key);
void insert_case1(rbtree *t, node_t *p);
void insert_case2(rbtree *t, node_t *p);
void insert_case3(rbtree *t, node_t *p);
void insert_case4(rbtree *t, node_t *p);
void insert_case5(rbtree *t, node_t *p);
static void rotate_left(rbtree *t, node_t *x);
static void rotate_right(rbtree *t, node_t *x);

node_t *make_granpa(node_t* p, rbtree *t){
  if((p!=t->nil)&&(p->parent != t->nil))
    return p->parent->parent;
  else
    return t->nil;
};
node_t *make_uncle(node_t* p, rbtree *t){
  node_t *granpa = make_granpa(p, t);
  if (granpa == t->nil)
    return t->nil; //할아버지가 없으면 삼촌도 없다
  if (p->parent == granpa->left)
    return granpa->right;
  else
    return granpa->left;
};

rbtree *new_rbtree(void) {
  // TODO: initialize struct if needed
  rbtree *p = (rbtree *)calloc(1, sizeof(rbtree));
  node_t *NIL = (node_t *)calloc(1, sizeof(node_t));
  NIL->color = RBTREE_BLACK;
  p->nil = p->root = NIL;
  return p;
}

void delete_rbtree(rbtree *t) {
  // TODO: reclaim the tree nodes's memory
  delete_rbtree_rep(t->nil, t->root);
  free(t->nil);
  free(t);
}
void delete_rbtree_rep(node_t *NIL, node_t *p){
  if (p != NIL){
    delete_rbtree_rep(NIL, p->left);
    delete_rbtree_rep(NIL, p->right);
    free(p);
  }
}

node_t* rbtree_insert(rbtree *t, const key_t key) {
  // TODO: implement insert
  node_t * Nil = t->nil;
  node_t * p = t->root;
  node_t * parent = Nil;
  
  while(p != Nil) //트리 위에서 값에따라 아래까지 내려감
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
  new_Node->left = new_Node->right = Nil;

  if(parent != Nil){
    if (parent->key > key) 
      parent->left = new_Node;
    else
      parent->right = new_Node;
  }
  else{
    t->root = new_Node;
  }

  insert_case1(t, new_Node);
  return new_Node;
}

void insert_case1(rbtree *t, node_t *p){
  if (p->parent == t->nil)
    p->color = RBTREE_BLACK;
  else
    insert_case2(t, p);
}
void insert_case2(rbtree *t, node_t *p){
  if (p->parent->color == RBTREE_BLACK)
    return;
  else
    insert_case3(t, p);
}
void insert_case3(rbtree *t, node_t *p){
  node_t *uncle = make_uncle(p, t), *granpa;
  if ((uncle != t->nil)&&(uncle->color==RBTREE_RED)){
    p->parent->color = uncle->color = RBTREE_BLACK;
    granpa = make_granpa(p, t);
    granpa->color = RBTREE_RED;
    insert_case1(t, granpa);
  }
  else
    insert_case4(t, p);
}
void insert_case4(rbtree *t, node_t *p){
  node_t *granpa = make_granpa(p, t);
  if((p==p->parent->right)&&(p->parent==granpa->left)){
    rotate_left(t, p->parent);
    p=p->left;
  }
  else if((p==p->parent->left)&&(p->parent==granpa->right)){
    rotate_right(t, p->parent);
    p=p->right;
  }
  insert_case5(t, p);
}
void insert_case5(rbtree *t, node_t *p){
  node_t *granpa = make_granpa(p, t);
  p->parent->color = RBTREE_BLACK;
  granpa->color = RBTREE_RED;
  if(p==p->parent->left)
    rotate_right(t, granpa);
  else
    rotate_left(t, granpa);
}

static void rotate_left(rbtree *t, node_t *x){ //g->x->y에서 g->y->x왼쪽
  node_t *y = x->right;
  x->right = y->left;
  if(y->left != t->nil)
    y->left->parent = x;
  y->parent = x->parent;

  if (x->parent == t->nil)
    t->root = y;
  else if (x == x->parent->left)
    x->parent->left = y;
  else
    x->parent->right = y;
  y->left = x;
  x->parent = y;
}
static void rotate_right(rbtree *t, node_t *x){ //g->x->y에서 g->y->x오른쪽
  node_t *y = x->left;
  x->left = y->right;
  if(y->right != t->nil)
    y->right->parent = x;
  y->parent = x->parent;

  if (x->parent == t->nil)
    t->root = y;
  else if (x == x->parent->right)
    x->parent->right = y;
  else
    x->parent->left = y;
  y->right = x;
  x->parent = y;
}

node_t *rbtree_find(const rbtree *t, const key_t key) {
  // TODO: implement find
  node_t * finder = t->root;
  while(finder != t->nil){
    if(finder->key == key)
      return finder;
    if(finder->key > key)
      finder = finder->left;
    else
      finder = finder->right;
  }
  return 0;
}

node_t *rbtree_min(const rbtree *t) {
  // TODO: implement find
  node_t * finder = t->root;
  node_t * previous;
  while(finder != t->nil){
    previous = finder;
    finder = finder->left;
  }
  return previous;
}

node_t *rbtree_max(const rbtree *t) {
  // TODO: implement find
  node_t * finder = t->root;
  node_t * previous;
  while(finder != t->nil){
    previous = finder;
    finder = finder->right;
  }
  return previous;
}

int rbtree_erase(rbtree *t, node_t *p) {
  // TODO: implement erase
  node_t *finder = t->root;
  node_t *previous;
  if (t->root == t->nil);
    return 1;
  while(finder->key != t->nil){
    previous = finder;
    if(finder->key > p->key){
      finder = finder->left;
    }
    else if(finder->key < p->key){
      finder = fidner->right;
    }
    else
      finder = fi
  }
  return 0;
}

int rbtree_to_array(const rbtree *t, key_t *arr, const size_t n) {
  // TODO: implement to_array
  return 0;
}
