def check(x, y, S):
    for d in range(3):
        W = S
        nx = x + dx[d]
        ny = y + dy[d]
        while 0 <= nx < 10 and 0 <= ny < 10 and arr[nx][ny] != '*':
            W += arr[nx][ny]
            nx = nx + dx[d]
            ny = ny + dy[d]
        if len(W) == 4:
            return W

T = int(input())
for tc in range(1, T+1):
    l = input()
    arr = [list(input()) for _ in range(10)]
    dx = [1, 0, 1]
    dy = [0, 1, 1]
    q = []
    words = []
    for i in range(10):
        for j in range(10):
            if arr[i][j] != '*': # 암호 발견하면
                s = arr[i][j]
                arr[i][j] = '*'
                # 3방향 체크 아래 오른쪽 대각선
                w = check(i, j, s)
                if w:
                    words.append(w)
    for i in range(3):
        words[i] = int(words[i], 16) # 10진수

    val = str(bin(words[0] + words[1] + words[2])[2:])
    cnt = 0
    for i in range(len(val)):
        if val[i] == '1':
            cnt += 1
    if cnt % 3 == 0:
        print(f'#{tc} Pass')
    else:
        print(f'#{tc} Fail')












