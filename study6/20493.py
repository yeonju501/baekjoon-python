import sys
sys.stdin = open('20493_input.txt')

N, T = map(int, input().split())
x = y = 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
d = temp = t = 0
for i in range(N):
    t, s = input().split()
    t = int(t)
    x = x + dx[d] * (t - temp)
    y = y + dy[d] * (t - temp)
    if s == 'right':
        d = (d+1) % 4
    elif s == 'left':
        d = (d-1) % 4
    temp = t
else:
    x = x + dx[d] * (T - t)
    y = y + dy[d] * (T - t)

print(x, y)

