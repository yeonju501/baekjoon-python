import sys
sys.stdin = open('1569_input.txt')

def check(min_x, max_x, min_y, max_y):
    for i in range(T):
        if (min_x <= xs[i] <= max_x and min_y <= ys[i] <= max_y) and (xs[i] == min_x or xs[i] == max_x or ys[i] == min_y or ys[i] == max_y):
            continue
        else:
            return False
    return True


T = int(input())
xs = []
ys = []
for _ in range(T):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
max_x = max(xs)
min_x = min(xs)
max_y = max(ys)
min_y = min(ys)
side = max(max_x-min_x, max_y-min_y)
c1 = check(min_x, min_x + side, min_y, min_y+side)
c2 = check(max_x-side, max_x, max_y-side, max_y)
if c1 or c2:
    print(side)
else:
    print(-1)
