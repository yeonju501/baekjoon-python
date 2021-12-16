import sys
sys.stdin = open('10844_input.txt')

N = int(input())
arr = [[0] * 10 for _ in range(N+1)]
arr[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N+1):
    arr[i][0] = arr[i-1][1]
    arr[i][9] = arr[i-1][8]
    for j in range(1, 9):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]

print(sum(arr[N]) % 1000000000)

