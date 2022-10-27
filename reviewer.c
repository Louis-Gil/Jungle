#include "rbtree.h"

#include <stdlib.h>

rbtree *new_rbtree(void)
{
  // rb 트리 1개 만큼의 동적 메모리 할당. 포인터 p는 생성된 rbtree 1개의 메모리 주소를 가리킨다.
  rbtree *p = (rbtree *)calloc(1, sizeof(rbtree));
  // nil을 사용하면 color를 편하게 지정

  // rbtree의 nil에 node_t만큼의 메모리를 동적으로 할당
  p->nil = (node_t *)calloc(1, sizeof(node_t));

  // 처음 root값은 NULL임
  p->root = p->nil;

  // RB트리에서 nil 노드의 color은 black이다.
  p->nil->color = RBTREE_BLACK;
  return p;
}
void delete_node(node_t *node, rbtree *tree)
{
  if (node != tree->nil)
  {
    delete_node(node->left, tree);
    delete_node(node->right, tree);
    free(node);
  }
}

void delete_rbtree(rbtree *t)
{
  delete_node(t->root, t);
  free(t->nil); // 반납한다.
  free(t);
}

void left_rotation(rbtree *t, node_t *node)
{
  node_t *y = node->right;
  node->right = y->left; // node, y.l 연결

  if (y->left != t->nil)
    y->left->parent = node; // node, y.l 연결

  y->parent = node->parent;   // node.p, y.p 대체하기
  if (node->parent == t->nil) // node가 root 인 경우
    t->root = y;
  else if (node == node->parent->left) // node가 왼쪽 자식인 경우
    node->parent->left = y;
  else // node가 오른쪽 자식인 경우
    node->parent->right = y;
  y->left = node;   // y 왼쪽 자식에 node 연결해주기
  node->parent = y; // y 왼쪽 자식에 node 연결해주기
}
void right_rotation(rbtree *t, node_t *node)
{
  node_t *y = node->left;
  node->left = y->right; // node, y.l 연결

  if (y->right != t->nil)
    y->right->parent = node; // node, y.l 연결

  y->parent = node->parent;   // node.p, y.p 대체하기
  if (node->parent == t->nil) // node가 root 인 경우
    t->root = y;
  else if (node == node->parent->left) // node가 왼쪽 자식인 경우
    node->parent->left = y;
  else // node가 오른쪽 자식인 경우
    node->parent->right = y;
  y->right = node;  // y 왼쪽 자식에 node 연결해주기
  node->parent = y; // y 왼쪽 자식에 node 연결해주기
}

void rbtree_insert_fixup(rbtree *t, node_t *z)
{
  while (z->parent->color == RBTREE_RED)
  {
    if (z->parent == z->parent->parent->left)
    {
      node_t *uncle = z->parent->parent->right;
      if (uncle->color == RBTREE_RED)
      {
        z->parent->color = RBTREE_BLACK;
        uncle->color = RBTREE_BLACK;
        z->parent->parent->color = RBTREE_RED;
        z = z->parent->parent;
      }
      else
      {
        if (z == z->parent->right)
        {
          z = z->parent;
          left_rotation(t, z);
        }
        z->parent->color = RBTREE_BLACK;
        z->parent->parent->color = RBTREE_RED;
        right_rotation(t, z->parent->parent);
      }
    }
    else
    {
      node_t *uncle = z->parent->parent->left;
      if (uncle->color == RBTREE_RED)
      {
        z->parent->color = RBTREE_BLACK;
        uncle->color = RBTREE_BLACK;
        z->parent->parent->color = RBTREE_RED;
        z = z->parent->parent;
      }
      else
      {
        if (z == z->parent->left)
        {
          z = z->parent;
          right_rotation(t, z);
        }
        z->parent->color = RBTREE_BLACK;
        z->parent->parent->color = RBTREE_RED;
        left_rotation(t, z->parent->parent);
      }
    }
  }
  t->root->color = RBTREE_BLACK;
}

node_t *rbtree_insert(rbtree *t, const key_t key)
{
  node_t *z = (node_t *)malloc(sizeof(node_t));
  node_t *pre_node = t->nil;
  node_t *cur_node = t->root;
  // key의 위치에 맞는 곳에 접근
  while (cur_node != t->nil)
  {
    pre_node = cur_node;
    if (key < cur_node->key)
      cur_node = cur_node->left;
    else
      cur_node = cur_node->right;
    // key값이 같은 값이 들어가면 저장한다.
  }
  // z의 parent를 설정
  z->parent = pre_node;
  // t에 root가 없을 경우
  if (pre_node == t->nil)
    t->root = z;
  // parent의 child를 설정
  else if (key < pre_node->key)
    pre_node->left = z;
  else
    pre_node->right = z;
  // z값 초기화
  z->key = key;
  z->left = t->nil;
  z->right = t->nil;
  z->color = RBTREE_RED; // 레드트리 규칙
  rbtree_insert_fixup(t, z);
  return z;
}

node_t *rbtree_find(const rbtree *t, const key_t key)
{
  if (t->root == t->nil)
  {
    return NULL; // nil 개념을 사용하여 전체 코드를 짰으나, 탐색 테스트 케이스에서 NULL을 요구한다. 따라서 t->nil이 아니라 NULL로 작성하였다.
  }
  node_t *cur_node = t->root;

  while (cur_node != t->nil)
  {
    if (cur_node->key > key)
    {
      cur_node = cur_node->left;
    }
    else if (cur_node->key < key)
    {
      cur_node = cur_node->right;
    }
    else
    {
      return cur_node;
    }
  } // 반복문을 탈출했을때 cur_node가 nil 노드이다.

  return NULL; // 찾으려는 값이 없다.
}

node_t *rbtree_min(const rbtree *t)
{
  node_t *cur_node = t->root;

  while (cur_node->left != t->nil)
  {
    cur_node = cur_node->left; // 왼쪽으로 계속해서 탐색해라.
  }                            // 탈출했을때 cur_node->left 가 nil이다.

  return cur_node;
}

node_t *rbtree_max(const rbtree *t)
{
  node_t *cur_node = t->root;

  while (cur_node->right != t->nil)
  {
    cur_node = cur_node->right; // 오른쪽으로 계속해서 탐색해라.
  }                             // 탈출했을때 cur_node->left 가 nil이다.

  return cur_node;
}

void rbtree_transplant(rbtree *t, node_t *removed, node_t *successor)
{
  if (removed->parent == t->nil)
  { // removed 가 root 노드라면, 단순하게 successor 가 root 노드가 되면 된다.
    t->root = successor;
  }
  else if (removed == removed->parent->left)
  {
    removed->parent->left = successor;
  }
  else
  {
    removed->parent->right = successor;
  }

  successor->parent = removed->parent;
  // successor의 parent가 removed의 parent를 향하도록 한다. 이 때 removed->parent가 t->nil이더라도 상관없다.
  // rbtree, 그리고 이 코드에서는 nil 개념을 사용하니까
}

node_t *find_min_successor(rbtree *t, node_t *y)
{
  while (y->left != t->nil)
  {
    // y의 왼쪽 자식이 nil이 아닐 때까지 계속 파고들어간다.
    y = y->left;
  }

  // y의 왼쪽 자식이 nil이라면 멈추기 때문에(y가 nil이면 멈추는게 아니라) y는 유의미한 값을 가진 노드를 가르키는 주소값이다. 여기서는 successor라고 보면 된다.
  return y;
}

// [삭제_fixup]
// 노드를 삭제하고 나면 특성 2, 4, 5를 위반했을 수도 있으니 재조정이 필요하다.
void rbtree_erase_fixup(rbtree *t, node_t *successor)
{
  node_t *sibling; // x(successor)의 형제 노드를 가리키는 sibling 포인터를 미리 선언한다.

  while (successor != t->root && successor->color == RBTREE_BLACK)
  { // x가 root가 되면 단순히 그냥 검은색으로 바꾸면된다. 그리고 while문 아래는 x가 doubly black일 떄 이뤄진다.
    // doubly black인 x가 왼쪽 자식일 때
    if (successor == successor->parent->left)
    {
      sibling = successor->parent->right;

      // <경우 1> : 경우 2, 3, 4로 위임 가능
      if (sibling->color == RBTREE_RED)
      {
        sibling->color = RBTREE_BLACK;
        successor->parent->color = RBTREE_RED;
        left_rotation(t, successor->parent);
        sibling = successor->parent->right; // 회전을 끝내고 난 후에는 successor->parent->right가 새로운 노드가 되고
                                            //밑의 if, else if, else 중 한 가지, 즉 경우 2, 3, 4의 한 가지로 위임된다.
      }

      // 위의 if문을 만나지 않았으므로, sibling->color == RBTREE_BLACK인 경우이다.
      // <경우 2> : 경우 1, 2, 3, 4로 위임 가능
      // successor->parent로 짬 때리는 경우이다.
      if (sibling->left->color == RBTREE_BLACK && sibling->right->color == RBTREE_BLACK)
      {
        sibling->color = RBTREE_RED;   // x의 extra black을 successor->parent로 넘긴다. 그러면서 w는 red가 된다.
        successor = successor->parent; // 새롭게 doubly black 혹은 red and black이 successor->parent이 짬 맞아서 재조정을 진행하도록 위임한다.
      }
      else
      {

        // <경우 3> : 경우 4로 위임 가능
        if (sibling->right->color == RBTREE_BLACK)
        {
          sibling->left->color = RBTREE_BLACK;
          sibling->color = RBTREE_RED;
          right_rotation(t, sibling);
          sibling = successor->parent->right;
        }

        // <경우 4> : 특성이 위반되는 것을 해결한다. 경우 4는 다른 경우로 위임되지 않고 위반을 해결(특성을 만족)한다.
        sibling->color = successor->parent->color;
        successor->parent->color = RBTREE_BLACK;
        sibling->right->color = RBTREE_BLACK;
        left_rotation(t, successor->parent);
        successor = t->root; // 경우 4를 거치면 특성 위반이 해결되는 것이므로 x를 root로 설정하여 while문을 빠져나가도록 한다.
      }
    }
    else
    {
      sibling = successor->parent->left;

      // <경우 1>
      if (sibling->color == RBTREE_RED)
      {
        sibling->color = RBTREE_BLACK;
        successor->parent->color = RBTREE_RED;
        right_rotation(t, successor->parent);
        sibling = successor->parent->left;
      }

      // <경우 2>
      if (sibling->right->color == RBTREE_BLACK && sibling->left->color == RBTREE_BLACK)
      {
        sibling->color = RBTREE_RED;
        successor = successor->parent;
      }
      else
      {

        // <경우 3>
        if (sibling->left->color == RBTREE_BLACK)
        {
          sibling->right->color = RBTREE_BLACK;
          sibling->color = RBTREE_RED;
          left_rotation(t, sibling);
          sibling = successor->parent->left;
        }

        // <경우 4>
        sibling->color = successor->parent->color;
        successor->parent->color = RBTREE_BLACK;
        sibling->left->color = RBTREE_BLACK;
        right_rotation(t, successor->parent);
        successor = t->root;
      }
    }
  }

  successor->color = RBTREE_BLACK; // x가 root 노드이거나, red and black이면 해당 코드를 만나서 black이 되고 특성들을 만족시키게 된다.
}

int rbtree_erase(rbtree *t, node_t *target)
{
  node_t *removed = target; // z는 우리가 삭제하고자 하는 노드의 주소값, y는 대체할 노드를 탐색한 후 그 대체할 노드를 가르키는 주소값(y는 target 혹은 successor)

  // 나중에 y의 color, 즉 우리가 삭제하고자 하는 노드에 들어갈(대체할), 실제로 삭제하는 노드의 색깔이다. 이는 레드 블랙 트리의 삭제 원리에 따라 블랙일 경우 문제가 되기에 미리 저장해둔다.
  color_t removed_original_color = removed->color; // 해당 코드에서는 나중에 y의 색깔이 z의 색깔로 되기 때문에 미리 저장해둬야 한다. 이 코드가 바뀌지 않으면, target 바로 자신이 실제로 삭제된다는 얘기이다. 그 경우는 자식 노드가 0개 혹은 1개일 때이므로 밑의 if문과 else if문을 말한다.

  node_t *successor; // x는 y의 자식으로, 여기서는 오른쪽 서브트리에서 가장 작은 값을 가진 노드를 탐색할 것이므로 removed(successor)의 오른쪽 자식이다.

  if (target->left == t->nil)
  {                                          // z의 자식이 오른쪽 자식 1개뿐이라면
    successor = target->right;               // 그 z의 자식 x를
    rbtree_transplant(t, target, successor); // 그냥 target 자리에 심으면 된다.
  }
  else if (target->right == t->nil)
  {
    successor = target->left;
    rbtree_transplant(t, target, successor);
  }
  else
  {
    removed = find_min_successor(t, target->right); // z의 오른쪽 자식에서, 즉 오른쪽 서브 트리에서 successor를 찾는다. 이는 z보다 크지만 오른쪽 서브 트리에서 가장 작은, target 바로 다음으로 큰 successor를 찾는 것이다.
    removed_original_color = removed->color;        // 여기서는 이제 실제로 삭제될 노드 successor의 색을 저장해둬야 한다.
    successor = removed->right;                     // y는 실제로 삭제될 거니까, y의 자리에 x가 대체자로 올라와야 한다.

    if (removed->parent == target)
    { // 이건 왜 하는지 잘 모르겠다. transplant하면서 자연스럽게 부모가 바뀌지 않나? ( -> 이건 successor가 값이 있는 경우만 해당한다. )
      // successor가 nil일 경우를 대비해서 해주는 것이다.
      successor->parent = removed;
    }
    else
    {
      rbtree_transplant(t, removed, successor); // z에 y를 심기 전에, 먼저 y의 자리에 y의 자식을 심는다. 그렇지 않으면 y는 자식이 딸린 채로 z에 심어지기 때문이다. 해당 코드를 실행하면 removed 노드 1개만 딱 떼어져 있다고 생각하면 편할 듯 하다.
      removed->right = target->right;           // z에 y를 심기 전에 행하는 사전 작업이다.
      removed->right->parent = removed;         // 우리가 방금 removed 하나만 딱 둥그러니 떼놨기 때문에 y의 자식과 그 자식의 부모를 y로 향하게 설정해줘야 한다.
    }                                           // 근데 왜 오른쪽 자식만 먼저 하지?

    rbtree_transplant(t, target, removed); // 이제 z에 y를 심는다. 정확히는 z의 부모는 이제 z가 아니라 y를 가르키게 된다는 것이다.
    removed->left = target->left;
    removed->left->parent = removed;
    removed->color = target->color; // y는 z로 올라오고, y의 데이터는 유지한 체 색깔만 바뀐다. 즉 z의 색깔이 아니라 y의 색깔이 삭제되는 것이다. z에 y가 이식된 후, z의 색깔을 y에 심었으니까.
  }

  // 만약 위에서 삭제한 색이, 즉 실제로 삭제되는 노드인 y의 색이 red였다면 레드 블랙 트리 특성 5가지 중에서 위반되는 것은 없다.
  // 허나 black이었다면 위반하는 항목들이 있기 때문에 재조정이 필요하다. 단순히 생각하면 black을 삭제하여 red, red끼리 만나거나 특정 노드에서 리프 노드까지 만나는 black의 갯수가 달라질 수 있다.
  if (removed_original_color == RBTREE_BLACK)
  {
    rbtree_erase_fixup(t, successor); // 대체하는 노드 y의 자식인 x가 y의 자리로 올라오면서 이 x에 extra black을 부여한다. 이 extra black을 처리하면서 재조정하는 것이 fixup의 원리이므로 x를 인자로 넣는다.
  }

  free(target); // z가 삭제되고 그 자리에 y가 대체하는 것이므로 z를 free시켜준다.
  // TODO: implement erase
  return 0;
}

// [중위 순회]
void inorder_rbtree_to_array(const rbtree *t, node_t *x, key_t *arr, int *idx, const size_t n)
{
  if (x == t->nil)
  {
    return;
  }

  inorder_rbtree_to_array(t, x->left, arr, idx, n);
  if (*idx < n)
  {
    arr[(*idx)++] = x->key; // *idx는 0, 1, 2, 3...이다. 그리고 후위 연산자 ++이므로 0부터 인덱스가 시작된다.
  }
  else
  {
    return;
  }
  inorder_rbtree_to_array(t, x->right, arr, idx, n);
}

int rbtree_to_array(const rbtree *t, key_t *arr, const size_t n)
{
  node_t *x = t->root;
  if (x == t->nil)
  {
    return 0;
  }
  int cnt = 0;
  int *idx = &cnt;
  inorder_rbtree_to_array(t, x, arr, idx, n);

  return 0;
}