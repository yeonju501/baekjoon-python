arr = [list(map(int, input().split())) for _ in range(4)]
passenger = 0
max = 0
for i in range(len(arr)):
    passenger -= arr[i][0]
    passenger += arr[i][1]
    if max < passenger:
        max = passenger
print(max)

    