import sys
sys.stdin = open('2599_input.txt')

N = int(input())
b = []
g = []
ans = [[0] * 3 for _ in range(3)]
for _ in range(3):
    boy, girl = map(int, input().split())
    b.append(boy)
    g.append(girl)

if b[0] + g[0] > N or b[1] + g[1] > N or b[2] + g[2] > N:
    print(0)
elif (b[0] == N and g[0] != 0) or (b[1] == N and g[1] != 0) or (b[2] == N and g[2] != 0):
    print(0)
else:
    for i in range(3):
        flag = 0
        while b[i] != 0:
            for j in range(3):
                if i < j and b[i] and g[j] and not flag:
                    min_s = min(b[i], g[j])
                    ans[i][j] += min_s
                    b[i] -= min_s
                    g[j] -= min_s
                    flag = 1
                elif b[i] and g[j] and flag:
                    min_s = min(b[i], g[j])
                    ans[i][j] += min_s
                    b[i] -= min_s
                    g[j] -= min_s

    print(1)
    print(b, g)
    print(ans[0][1], ans[0][2])
    print(ans[1][0], ans[1][2])
    print(ans[2][0], ans[2][1])



