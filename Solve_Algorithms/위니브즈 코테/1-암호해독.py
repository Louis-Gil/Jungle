import sys
input = [
'   + -- + - + -   ',
'   + --- + - +   ',
'   + -- + - + -   ',
'   + - + - + - +   '
]
l = []

# ord() 문자->숫자, chr() 숫자->문자, int(숫자,2) 2진수변환
for i in input:
    l.append(chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'), 2)))
    
print(l)

# output1 = [f'{i} x {j} = {i*j}' for i in range(2,10) for j in range(1,10)]
# print(output1)

output2 = '111'.zfill(10)
print(output2)

output3 = [i.strip().replace(' ','').replace('+','1').replace('-','0')
           for i in input]
print(output3)

print(''.join(list(map(lambda x : chr(int(x,2)), output3))))

def f(x):
    return chr(int(x,2))
print(''.join(list(map(f, output3))))