# acmicpc.net/problem/1991
import sys
input = sys.stdin.readline

N = int(input())
tree = []
for _ in range(N):
    tree.append(input().split())

def preorder(node_num):
    print(tree[node_num][0], end = '')
    if tree[node_num][1] != '.':
        for i in range(N):
            if tree[i][0] == tree[node_num][1]:
                preorder(i)
                break
    if tree[node_num][2] != '.':
        for i in range(N):
            if tree[i][0] == tree[node_num][2]:
                preorder(i)
                break

def inorder(node_num):
    if tree[node_num][1] != '.':
        for i in range(N):
            if tree[i][0] == tree[node_num][1]:
                inorder(i)
                break
    print(tree[node_num][0], end = '')
    if tree[node_num][2] != '.':
        for i in range(N):
            if tree[i][0] == tree[node_num][2]:
                inorder(i)
                break

def postorder(node_num):
    if tree[node_num][1] != '.':
        for i in range(N):
            if tree[i][0] == tree[node_num][1]:
                postorder(i)
                break
    if tree[node_num][2] != '.':
        for i in range(N):
            if tree[i][0] == tree[node_num][2]:
                postorder(i)
                break
    print(tree[node_num][0], end = '')

preorder(0)
print()
inorder(0)
print()
postorder(0)
print()