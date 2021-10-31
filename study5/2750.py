import sys
sys.stdin = open('2750_input.txt')

N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = int(input())
for i in range(N-1):
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

for i in range(N):
    print(arr[i])
