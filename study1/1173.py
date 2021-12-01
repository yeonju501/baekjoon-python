import sys
sys.stdin = open('1173_input.txt')

"""
운동 or 맥박
운동 맥박 X+T
휴식 맥박 X-R
맥박은 m보다 낮아지지않고 M보다 커지지 않음
운동 N분
"""
minute = 0
N, m, M, T, R = map(int, input().split())
pulse = m
while N > 0:
    if M-m < T:
        minute = -1
        break
    if pulse + T <= M:
        N -= 1
        pulse += T
        minute += 1
    elif pulse - R <= m:
        pulse = m
        minute += 1
    elif pulse - R > m:
        pulse -= R
        minute += 1
print(minute)




