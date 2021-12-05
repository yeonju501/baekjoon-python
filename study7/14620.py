import sys
sys.stdin = open('14620_input.txt')

def p(k, hap):
    global ans
    if k == 2:
        if hap < ans:
            ans = hap
    else:
        for x in range(1, N-1):
            for y in range(1, N-1):
                if not visited[x][y] and not visited[x-1][y] and not visited[x+1][y] and not visited[x][y-1] and not visited[x][y+1]:
                    visited[x][y] = 1
                    visited[x - 1][y] = 1
                    visited[x + 1][y] = 1
                    visited[x][y - 1] = 1
                    visited[x][y + 1] = 1
                    p(k+1, hap + arr[x][y]+arr[x-1][y]+arr[x+1][y]+arr[x][y-1]+arr[x][y+1])
                    visited[x][y] = 0
                    visited[x - 1][y] = 0
                    visited[x + 1][y] = 0
                    visited[x][y - 1] = 0
                    visited[x][y + 1] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
ans = 987654321
for i in range(1, N-1):
    for j in range(1, N-1):
        visited[i][j] = 1
        visited[i - 1][j] = 1
        visited[i + 1][j] = 1
        visited[i][j - 1] = 1
        visited[i][j + 1] = 1
        p(0, arr[i][j]+arr[i-1][j]+arr[i+1][j]+arr[i][j-1]+arr[i][j+1])
        visited[i][j] = 0
        visited[i - 1][j] = 0
        visited[i + 1][j] = 0
        visited[i][j - 1] = 0
        visited[i][j + 1] = 0
print(ans)