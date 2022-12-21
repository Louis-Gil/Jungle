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