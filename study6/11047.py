import sys
sys.stdin = open('11047_input.txt')

N,money = map(int, input().split())
coins = [int(input()) for _ in range(N)]
ans = 0
for i in range(N-1, -1, -1):
    ans += money // coins[i]
    money %= coins[i]
print(ans)
