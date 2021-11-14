import sys
sys.stdin = open('9461_input.txt')


def f(n):
    if n >= 6 and len(p) <= n:
        p.append(f(n-1) + f(n-5))
    return p[n]
T = int(input())
p = [0, 1, 1, 1, 2, 2, 3]
for tc in range(T):
    N = int(input())
    print(f(N))