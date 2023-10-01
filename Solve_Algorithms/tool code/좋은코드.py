roads.sort(key = lambda x:x[1])
print(' '.join(f'{count[i]}' if i in count else '0' for i in find_lst))
