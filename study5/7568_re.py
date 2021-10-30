import sys
sys.stdin = open('7568_input.txt')

N = int(input())
person = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    rank = 1
    for j in range(N):
        if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            rank += 1
    print(rank, end=' ')


