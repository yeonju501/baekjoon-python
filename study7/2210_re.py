import sys
sys.stdin = open('2210_input.txt')

def dfs(i, j, num):
    if len(num) == 6:
        a.append(num)
        return
    else:
        for d in range(4):
            x = i + dx[d]
            y = j + dy[d]
            if 0 <= x < 5 and 0 <= y < 5:
                dfs(x, y, num+arr[x][y])

dx = [-1, 0, 1, 0] #상우하좌
dy = [0, 1, 0, -1]
arr = [input().split() for _ in range(5)]
a = []
for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])

print(len(set(a)))
