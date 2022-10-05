import sys
# sys.stdin = open('02\input.txt', 'r')
trees_num, needs = (map(int, sys.stdin.readline().split()))
trees_list = list(map(int, sys.stdin.readline().split()))
# print(trees_num, needs, trees_list)

# def cut_tree(trees_list, needs, start, end):
#     while start <= end:
#         pin = (start + end)//2
#         mount = 0
#         for i in trees_list:
#             if pin < i : mount += (i - pin)
#         if mount >= needs:
#             start = pin + 1
#         else :
#             end = pin - 1
#     return end


# start = 1
# end = max(trees_list)
# print(cut_tree(trees_list, needs, start, end))

def test(trees_list, needs, start, end):
    result = 0
    while start <= end:
        pin = (start+end)//2
        mount = 0
        for i in trees_list:
            if pin < i : mount += (i-pin)
        if mount >= needs:
            start = pin +1
            result = pin
        else :
            end = pin -1
    return result

start = 1
end = max(trees_list)
print(test(trees_list, needs, start, end))