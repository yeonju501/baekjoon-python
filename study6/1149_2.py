import sys
sys.stdin = open('1149_input.txt')

N = int(input())
h = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    h[i][0] = h[i][0] + min(h[i-1][1], h[i-1][2])
    h[i][1] = h[i][1] + min(h[i-1][0], h[i-1][2])
    h[i][2] = h[i][2] + min(h[i-1][0], h[i-1][1])
print(min(h[N-1]))
