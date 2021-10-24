import sys
sys.stdin = open('15662_input.txt')

def rotate(n, d):
    t = [0]*8
    if d == 1:
        for i in range(8):
            t[(i+1)%8] = a[n][i]
    else:
        for i in range(8):
            t[i] = a[n][(i+1)%8]
    for i in range(8):
        a[n][i] = t[i]

def solve():
    for _ in range(int(input())):
        n, d = map(int, input().split())
        direct = [0]*t
        direct[n-1] = d
        for i in range(n-1, t-1):
            if a[i][2] != a[i+1][6]:
                direct[i+1] = -direct[i]
            else:
                break
        for i in range(n-1, 0, -1):
            if a[i][6] != a[i-1][2]:
                direct[i-1] = -direct[i]
            else:
                break
        for i in range(t):
            if direct[i]:
                rotate(i, direct[i])

t = int(input())
a = [list(input().strip()) for _ in range(t)]
solve()
ans = 0
for i in range(t):
    if a[i][0] == '1':
        ans += 1
print(ans)
