import sys
sys.stdin = open('1931_input.txt')

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x:(x[1], x[0]))
cnt = 1
end = meetings[0][1]
for i in range(1, N):
    if meetings[i][0] >= end:
        cnt += 1
        end = meetings[i][1]
print(cnt)