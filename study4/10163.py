# 1001칸
import sys
# sys.stdin = open('10163_input.txt')
input = sys.stdin.readline
T = int(input())
arr = [[0] * 1001 for _ in range(1001)]
for t in range(1, T+1):
    y, x, w, h = map(int, input().split())
    for i in range(h):
        for j in range(w):
            arr[x+i][y+j] = t
ts = [0] * (T+1)
for i in range(1001):
    for j in range(1, T+1):
        ts[j] += arr[i].count(j)

for i in range(1,T+1):
    print(ts[i])
