#include "rbtree.h"
#include <stdlib.h>

void delete_rbtree(rbtree *t);
void delete_rbtree_rep(node_t *NIL, node_t *p);
node_t *rbtree_insert(rbtree *t, const key_t key);
void rbtree_insert_sub(rbtree *t, node_t *p);
static void rotate_left(rbtree *t, node_t *x);
static void rotate_right(rbtree *t, node_t *x);
int rbtree_erase(rbtree *t, node_t *p);
node_t *rbtree_erase_find_node_max(rbtree *t, node_t *p);
void rbtree_erase_transplant(rbtree *t, node_t *p, node_t *successor);
void rbtree_erase_fixup(rbtree *t, node_t *p);

node_t *make_granpa(node_t *p, rbtree *t)
{
  if ((p != t->nil) && (p->parent != t->nil))
    return p->parent->parent;
  else
    return t->nil;
};
node_t *make_uncle(node_t *p, rbtree *t)
{
  node_t *granpa = make_granpa(p, t);
  if (granpa == t->nil)
    return t->nil; //할아버지가 없으면 삼촌도 없다
  if (p->parent == granpa->left)
    return granpa->right;
  else
    return granpa->left;
};

rbtree *new_rbtree(void)
{
  // TODO: initialize struct if needed
  rbtree *p = (rbtree *)calloc(1, sizeof(rbtree));
  node_t *NIL = (node_t *)calloc(1, sizeof(node_t));
  NIL->color = RBTREE_BLACK;
  p->nil = p->root = NIL;
  return p;
}

void delete_rbtree(rbtree *t)
{
  // TODO: reclaim the tree nodes's memory
  delete_rbtree_rep(t->nil, t->root);
  free(t->nil);
  free(t);
}
void delete_rbtree_rep(node_t *NIL, node_t *p)
{
  if (p != NIL)
  {
    delete_rbtree_rep(NIL, p->left);
    delete_rbtree_rep(NIL, p->right);
    free(p);
  }
}

node_t *rbtree_insert(rbtree *t, const key_t key)
{
  // TODO: implement insert
  node_t *temp = t->nil;
  node_t *p = t->root;

  while (p != t->nil) //트리 위에서 값에따라 아래까지 내려감
  {
    temp = p;
    if (p->key > key)
      p = p->left;
    else
      p = p->right;
  }

  node_t *new_Node = (node_t *)calloc(1, sizeof(node_t));
  new_Node->color = RBTREE_RED;
  new_Node->key = key;
  new_Node->parent = temp;
  new_Node->left = new_Node->right = t->nil;

  if (temp == t->nil)
  {
    t->root =new_Node;
  }
  else if(new_Node->key < temp->key)
  {
    temp->left = new_Node;
  }
  else
  {
    temp->right = new_Node;
  }


  rbtree_insert_sub(t, new_Node);
  return new_Node;
}

void rbtree_insert_sub(rbtree *t, node_t *p)
{
  node_t *uncle;
  while(p->parent->color == RBTREE_RED)
  {
    if (p->parent == p->parent->parent->left)
    {
      uncle = p->parent->parent->right;
      if (uncle->color == RBTREE_RED)
      {
        p->parent->color = RBTREE_BLACK;
        uncle->color = RBTREE_BLACK;
        p->parent->parent->color = RBTREE_RED;
        p = p->parent->parent;
      }
      else 
      {
        if (p == p->parent->right)
        {
          p = p->parent;
          rotate_left(t, p);
        }
        p->parent->color = RBTREE_BLACK;
        p->parent->parent->color = RBTREE_RED;
        rotate_right(t,p->parent->parent);
      }
    }
    else
    {
      uncle = p->parent->parent->left;
      if (uncle->color == RBTREE_RED)
      {
        p->parent->color = RBTREE_BLACK;
        uncle->color = RBTREE_BLACK;
        p->parent->parent->color = RBTREE_RED;
        p = p->parent->parent;
      }
      else 
      {
        if (p == p->parent->left)
        {
          p = p->parent;
          rotate_right(t, p);
        }
        p->parent->color = RBTREE_BLACK;
        p->parent->parent->color = RBTREE_RED;
        rotate_left(t,p->parent->parent);
      }
    }
  }
  t->root->color = RBTREE_BLACK;
}


static void rotate_left(rbtree *t, node_t *x)
{ // g->x->y에서 g->y->x왼쪽
  node_t *y = x->right;
  x->right = y->left;
  if (y->left != t->nil)
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
static void rotate_right(rbtree *t, node_t *x)
{ // g->x->y에서 g->y->x오른쪽
  node_t *y = x->left;
  x->left = y->right;
  if (y->right != t->nil)
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

node_t *rbtree_find(const rbtree *t, const key_t key)
{
  // TODO: implement find
  node_t *finder = t->root;
  while (finder != t->nil)
  {
    if (finder->key == key)
      return finder;
    if (finder->key > key)
      finder = finder->left;
    else
      finder = finder->right;
  }
  return NULL;
}
node_t *rbtree_min(const rbtree *t)
{
  // TODO: implement find
  node_t *finder = t->root;
  node_t *previous;
  while (finder != t->nil)
  {
    previous = finder;
    finder = finder->left;
  }
  return previous;
}
node_t *rbtree_max(const rbtree *t)
{
  // TODO: implement find
  node_t *finder = t->root;
  node_t *previous;
  while (finder != t->nil)
  {
    previous = finder;
    finder = finder->right;
  }
  return previous;
}

int rbtree_erase(rbtree *t, node_t *p)
{
  node_t *temp = p;
  node_t *tofix;
  color_t del_color = temp->color;
  if (p->left == t->nil)
  {
    tofix = p->right;
    rbtree_erase_transplant(t, p, p->right);
  }
  else if(p->right == t->nil)
  {
    tofix = p->left;
    rbtree_erase_transplant(t, p, p->left);
  }
  else
  {
    temp = rbtree_erase_find_node_max(t, p->right);
    del_color = temp->color;
    tofix = temp->right;
    if(temp->parent == p)
    {
      tofix->parent = temp;
    }
    else 
    {
      rbtree_erase_transplant(t, temp, temp->right);
      temp->right = p->right;
      temp->right->parent = temp;
    }
    rbtree_erase_transplant(t, p, temp);
    temp->left = p->left;
    temp->left->parent = temp;
    temp->color = p->color;
  }

  if(del_color==RBTREE_BLACK)
  {
    rbtree_erase_fixup(t,tofix);  
  }

  free(p);
  return 0;
}

node_t *rbtree_erase_find_node_max(rbtree *t, node_t *p)
{
  while (p->left != t->nil)
  {
    p = p->left;
  }
  return p;
}

void rbtree_erase_transplant(rbtree *t, node_t *p, node_t *successor)
{
  if (p->parent == t->nil)
    t->root = successor;
  else if (p == p->parent->left)
  {
    p->parent->left = successor;
  }
  else
  {
    p->parent->right = successor;
  }
  successor->parent = p->parent;
}

void rbtree_erase_fixup(rbtree *t, node_t *p)
{
  node_t *sachon;
  while((p != t->root) && (p->color == RBTREE_BLACK))
  {
    if(p == p->parent->left)
    {
      sachon = p->parent->right;
      if(sachon->color == RBTREE_RED)
      {
        sachon->color = RBTREE_BLACK;
        p->parent->color = RBTREE_RED;
        rotate_left(t, p->parent);
        sachon = p->parent->right;
      }
      if ((sachon->left->color == RBTREE_BLACK) && (sachon->right->color == RBTREE_BLACK))
      {
        sachon->color = RBTREE_RED;
        p = p->parent;
      }
      else 
      {
        if(sachon->right->color == RBTREE_BLACK) 
        {
          sachon->left->color = RBTREE_BLACK;
          sachon->color = RBTREE_RED;
          rotate_right(t, sachon);
          sachon = p->parent->right;
        }
        sachon->color = p->parent->color;
        p->parent->color = RBTREE_BLACK;
        sachon->right->color = RBTREE_BLACK;
        rotate_left(t, p->parent);
        p = t->root;
      }
    }

    else
    {
      sachon = p->parent->left;
      if(sachon->color == RBTREE_RED)
      {
        sachon->color = RBTREE_BLACK;
        p->parent->color = RBTREE_RED;
        rotate_right(t, p->parent);
        sachon = p->parent->left;
      }
      if ((sachon->right->color == RBTREE_BLACK) && (sachon->left->color == RBTREE_BLACK))
      {
        sachon->color = RBTREE_RED;
        p = p->parent;
      }
      else 
      {
        if(sachon->left->color == RBTREE_BLACK) //else if?, else?
        {
          sachon->right->color = RBTREE_BLACK;
          sachon->color = RBTREE_RED;
          rotate_left(t, sachon);
          sachon = p->parent->left;
        }
        sachon->color = p->parent->color;
        p->parent->color = RBTREE_BLACK;
        sachon->left->color = RBTREE_BLACK;
        rotate_right(t, p->parent);
        p = t->root;

      }
    }
  }
  p->color = RBTREE_BLACK;
}

int inorder_search(const rbtree *t, node_t *p, int idx, key_t *arr, int n)
{
  if (p == t->nil || idx >= n)
    return idx;
  // printf("%d ", p->key);
  idx = inorder_search(t, p->left, idx, arr, n);
  arr[idx++] = p->key;
  idx = inorder_search(t, p->right, idx, arr, n);
  return idx;
}

int rbtree_to_array(const rbtree *t, key_t *arr, const size_t n)
{
  // TODO: implement to_array
  inorder_search(t,t->root,0,arr,n);
  return 0;
}
