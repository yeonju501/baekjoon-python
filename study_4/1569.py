import sys
sys.stdin = open('1569_input.txt')

T = int(input())
xs = []
ys = []
for _ in range(T):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
h_max = max(xs)
h_min = min(xs)
v_max = max(ys)
v_min = min(ys)
side = max(v_max-v_min, h_max-h_min)
flag = 0
for i in range(T):
    if h_min <= xs[i] <= h_min+side and v_min <= ys[i] <= v_min+side:
        if xs[i] == h_min or xs[i] == h_min+side or ys[i] == v_min or ys[i] == v_min+side:
            continue
        else:
            flag = 1
    if flag and h_max-side <= xs[i] <= h_max and v_max-side <= ys[i] <= v_max:
        if xs[i] == h_max or xs[i] == h_max-side or ys[i] != v_max or ys[i] != v_max-side:
            flag = 0
            continue
        else:
            flag = 1
if flag:
    print(-1)
else:
    print(side)

