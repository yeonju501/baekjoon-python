import sys
sys.stdin = open('11559_input.txt')

def bfs():
    for i in range(12):
        for j in range(6):
            if arr[i][j] == '.':




arr = [list(input()) for _ in range(12)]
visited = [[0] * 6 for _ in range(12)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
bfs()