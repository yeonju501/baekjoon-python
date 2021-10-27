import sys
sys.stdin = open('2456_input.txt')

N = int(input())
arr = [[0] * 4 for _ in range(3)]
for _ in range(N):
    nums = list(map(int, input().split()))
    for i in range(3):
        if nums[i] == 3:
            arr[i][1] += 1
            arr[i][0] += 3
        elif nums[i] == 2:
            arr[i][2] += 1
            arr[i][0] += 2
        else:
            arr[i][3] += 1
            arr[i][0] += 1
cnt = j = i = 0
m_idx = 0
for j in range(3):
    cnt = 0
    m = max(arr, key=lambda x:x[j])
    for i in range(3):
        if arr[i][j] == m[j]:
            cnt += 1
            m_idx = i
        else:
            arr[i][j+1] = 0
    if cnt == 1:
        print(m_idx + 1, m[0])
        break
else:
    print(0, m[0])



