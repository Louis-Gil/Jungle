import sys
N = int(sys.stdin.readline())

points = []
for _ in range(N):
    c, r = list(map(int, sys.stdin.readline().split()))
    points.append(("L", c-r))
    points.append(("R", c+r))

# 좌표 기준 정렬    
points.sort(key=lambda p: (-p[1], p[0]), reverse=True)
print(points)
# 차례대로 돌며 확인
stack = []
area = 1
for curr in points:
    # 왼쪽끝인 경우
    if curr[0] == "L":
        stack.append(curr)
        continue
    # 오른쪽끝인 경우
    cum_width = 0
    while stack:
        prev = stack.pop()
        # 본인 내부에 원이 있었으면, 해당 원의 너비를 누적
        if prev[0] == "C":
            cum_width += prev[1]        
        # R이 나올 때마다 L를 pop해주므로 처음 만난 L이 본인과 동일한 원에서 나온 값
        elif prev[0] == "L":
            # 원의 너비 계산
            width = curr[1] - prev[1]
            # 내부에 있는 원들의 너비 합산이 본인의 너비와 일치하는지 확인
            if width == cum_width:
                area += 2
            else:
                area += 1
            # 다른 원에 포함될 수 있으므로 추가
            stack.append(("C", width)) 
            break
    
print(area)