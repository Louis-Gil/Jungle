import sys
sys.stdin = open('03\input.txt', 'r')
input = sys.stdin.readlines()
sys.setrecursionlimit(10**6)
tree = []

def postorder(start, end):
    if start > end:
        return
    current = tree[start]

    if current>tree[end]:
        postorder(start+1, end)
        print(current)
        return
    
    mid = end + 1
    for i in range(start + 1, end + 1):
        if current < tree[i]:
            mid=i
            break
    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(current)


for i in input:
    tree.append(int(i.rstrip()))

postorder(0, len(tree)-1)