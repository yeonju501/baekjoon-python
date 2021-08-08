# 학생수대로 리스트 받아서 세어준다
import sys
x = int(sys.stdin.readline())
cls = []
for _ in range(x):
    cls.append(list(map(int, sys.stdin.readline().strip().split(' '))))
stu = [[0]*len(cls) for _ in range(5)]
for i in range(5):
    for j in range(len(cls)):
        stu[i][j] = cls[j][i]
m = 0
m_stu = 0
for i in range(len(cls)): # 사람수
    cnt = 0
    for j in range(len(cls[i])): # 반 번호
        cnt += stu[j].count(cls[i][j])-1
    if cnt > m:
        m = cnt
        m_stu = i
    elif cnt == m:
        continue
print(m_stu+1)


        

