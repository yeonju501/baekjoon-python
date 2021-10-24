import sys
sys.stdin = open('11564_input.txt')

k, a, b = map(int, input().split())
ans = 0
if a <= 0:
    ans += abs(a) // k + b // k + 1
else:
    if a % k == 0:
        ans += b // k - a // k + 1
    else:
        ans += b // k - a // k
print(ans)
