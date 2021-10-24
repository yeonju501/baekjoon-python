import sys
sys.stdin = open('17358_input.txt')

ans = 1
N = int(input())
for i in range(N-1, 0, -2):
    ans *= i
    ans %= 1000000007
print(ans)