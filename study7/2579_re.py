import sys
sys.stdin = open('2579_input.txt')
# input = sys.stdin.readline
N = int(input())
s = [0 for _ in range(301)]
dp = [0 for _ in range(301)]
for i in range(N):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1]+ s[2], s[0]+ + s[2])
for i in range(3, N):
    dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])
print(dp[N-1])

