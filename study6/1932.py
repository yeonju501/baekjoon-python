import sys
sys.stdin = open('1932_input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][j] = arr[i][j] + arr[i-1][j]
        elif j == len(arr[i])-1:
            arr[i][j] = arr[i][j] + arr[i-1][j-1]
        else:
            arr[i][j] = arr[i][j] + max(arr[i - 1][j - 1], arr[i - 1][j])
print(max(arr[-1]))



