# 이번학기 N분
# N 100점 짜리 과제 3분

# sys.stdin = open('17952_input.txt')
import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
s = []
for i in range(N):
    if arr[i][0] == 1:
        s.append([arr[i][1], arr[i][2] - 1])
    elif arr[i][0] == 0:
        if s:
            s[-1][1] -= 1
    if s and s[-1][1] == 0:
        ans += s[-1][0]
        s.pop()
print(ans)


