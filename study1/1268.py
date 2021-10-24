# 학생수대로 리스트 받아서 세어준다
import sys
sys.stdin = open('1268_input.txt')
# input = sys.stdin.readline
T = int(input())
l = [[0] * T for _ in range(T)]
a = []
arr = [list(map(int, input().split())) for _ in range(T)]
for i in range(T):
    for j in range(5):
        for z in range(T):
            if arr[i][j] == arr[z][j]:
                l[i][z] = 1

for i in range(T):
    s = l[i].count(1)
    a.append(s)

m = max(a)
print(a.index(m)+1)



        

