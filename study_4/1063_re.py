import sys
sys.stdin = open('1063_input.txt')

# 알파벳 하나와 숫자 하나 알파벳은 열 숫자는 행
"""
R : 한 칸 오른쪽으로
L : 한 칸 왼쪽으로
B : 한 칸 아래로
T : 한 칸 위로
RT : 오른쪽 위 대각선으로
LT : 왼쪽 위 대각선으로
RB : 오른쪽 아래 대각선으로
LB : 왼쪽 아래 대각선으로
"""
def check(s):
    if s == 'R':
        return 0
    elif s == 'L':
        return 1
    elif s == 'B':
        return 2
    elif s == 'T':
        return 3
    elif s == 'RT':
        return 4
    elif s == 'LT':
        return 5
    elif s == 'RB':
        return 6
    elif s == 'LB':
        return 7

K, S, N = map(str, input().split())
N = int(N)
arr = [[0] * 9 for _ in range(9)]
ki = ord(K[0])-64
kj = int(K[1])
si = ord(S[0])-64
sj = int(S[1])
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]
for i in range(N):
    n = check(input())
    di = ki + dx[n]
    dj = kj + dy[n]
    li = si + dx[n]
    lj = sj + dy[n]
    if di < 1 or di > 8 or dj < 1 or dj > 8:
        continue
    if di == si and dj == sj:
        if li < 1 or li > 8 or lj < 1 or lj > 8:
            continue
        si = li
        sj = lj
    ki = di
    kj = dj

print(chr(ki+64), kj, sep='')
print(chr(si+64), sj, sep='')





