import sys
sys.stdin = open('14425_input.txt')

N, M = map(int, input().split())
words = [input() for _ in range(N)]
cnt = 0
for i in range(M):
    letter = input()
    if letter in words:
        cnt += 1
print(cnt)