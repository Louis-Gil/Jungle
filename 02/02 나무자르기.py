import sys
sys.stdin = open('02\input.txt', 'r')

trees_num, needs = (map(int, sys.stdin.readline().split()))
trees_list = list(map(int, sys.stdin.readline().split()))

# print(trees_num, needs, trees_list, result)

def cut_tree(trees_list, needs, start, end):
    # 없는 경우는 없다
    global trees_num
    pin = (start + end)//2
    
    count = 0
    # 자른 나무 표에 넣기
    for i in trees_list:
        if pin < i : count += i - pin

    # 표 확인 후 다시 높이 세기
    if count == needs:
        return pin
    elif count > needs:
        return cut_tree(trees_list, needs, pin+1, end)
    else : 
        return cut_tree(trees_list, needs, start, pin-1)

start = 1
end = max(trees_list)
print(cut_tree(trees_list, needs, start, end))

