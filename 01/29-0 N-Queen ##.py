import sys
sys.stdin = open('01\input.txt', 'r')

n = int(sys.stdin.readline())

pos = [0] * n
flag1 = [False] * n
flag2 = [False] * (n*2-1)
flag3 = [False] * (n*2-1)

def nqueen(cur, num):
    for i in range(num):
        if ((flag1[i] is False) & (flag2[cur + i] is False) & (flag3[cur - i + 7] is False)):
            pos[cur] = i
            if cur == num -1:
                #put()
                for j in range(num):
                    print(f'{pos[j]:2}', end='')
                print()

            else :
                flag1[i] = flag2[cur + i] = flag3[cur - i + 7] = True
                nqueen(cur+1, num)
                flag1[i] = flag2[cur + i] = flag3[cur - i + 7] = False

nqueen(0, n)
# cur i
#(00)0, 0, 7 / (10)0, 
# pos[1] = 2 2