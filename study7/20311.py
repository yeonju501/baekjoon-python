import sys
sys.stdin = open('20311_input.txt')
# input = sys.stdin.readline
N, K = map(int, input().split())
c = list(map(int, input().split()))
arr = []
ans = []
for i in range(1, K+1):
    arr.append([c[i-1], i])
arr.sort(reverse=True)
for i in range(N//2):
    if len(ans) >= 2:
        ans.append(arr[0][1])
        arr[0][0] -= 1
        ans.append(arr[1][1])
        arr[1][0] -= 1
        if not arr[1][0]:
            arr.pop(1)
    else:
        ans.append(arr[0][1])
        arr[0][0] -= 1
        if not arr[0][0]:
            arr.pop(0)
    arr.sort(reverse=True)

if arr:
    print('-1')
else:
    print(*ans)