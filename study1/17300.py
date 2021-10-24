import sys
sys.stdin = open('17300_input.txt')
# input = sys.stdin.readline
l = int(input())
arr = list(map(int, input().split()))
visited = [0] * 10
adj = {
    1: [2, 4, 5, 6, 8],
    2: [1, 3, 4, 5, 6, 7, 9],
    3: [2, 4, 5, 6, 8],
    4: [1, 2, 3, 5, 7, 8, 9],
    5: [1, 2, 3, 4, 6, 7, 8, 9],
    6: [1, 2, 3, 5, 7, 8, 9],
    7: [2, 4, 5, 6, 8],
    8: [1, 3, 4, 5, 6, 7, 9],
    9: [2, 4, 5, 6, 8],
}
a = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [3, 5, 7], [1, 5, 9]]
for i in range(l):
    if visited[arr[i]] == 1: # 방문 했으면 못가
        print('NO')
        break
    elif i != 0 and arr[i-1] not in adj[arr[i]]:# 다음거가 지금거에 인접하지 않으면
        flag = 0
        for j in range(len(a)):
            if arr[i] in a[j] and arr[i - 1] in a[j]:
                for z in range(3):
                    if a[j][z] != arr[i] and a[j][z] != arr[i-1]:
                        if visited[a[j][z]] == 1:
                            visited[arr[i]] = 1
                            flag = 1
                            break
                        else:
                            flag = 0
        if flag == 0:
            print('NO')
            break
    visited[arr[i]] = 1
else:
    print('YES')