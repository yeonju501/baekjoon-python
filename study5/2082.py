import sys
sys.stdin = open('2082_input.txt')


def check(i, j):
    cnt = 0
    for x in range(5):
        for y in range(3):
            if nums[x][j+y] == '.' and time[x][i+y] == '#':
                ret[j//3] = 0
                return -1
            if nums[x][j+y] == time[x][i+y]:
                cnt += 1
    return j//3


nums = [
['#','#','#','.','.','#','#','#','#','#','#','#','#','.','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','#','.','.','#','.','.','#','.','.','#','#','.','#','#','.','.','#','.','.','.','.','#','#','.','#','#','.','#'],
['#','.','#','.','.','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','.','.','#','#','#','#','#','#','#'],
['#','.','#','.','.','#','#','.','.','.','.','#','.','.','#','.','.','#','#','.','#','.','.','#','#','.','#','.','.','#'],
['#','#','#','.','.','#','#','#','#','#','#','#','.','.','#','#','#','#','#','#','#','.','.','#','#','#','#','#','#','#'],
]
ret = [0] * 10
t = []
time = [list(input()) for _ in range(5)]
for i in range(0, 16, 4):
    for j in range(0, 30, 3):
        a = check(i, j)
        if a >= 0:
            t.append(a)
            break
for i in range(len(t)):
    if i == 2:
        print(':', end='')
    print(t[i], end='')




