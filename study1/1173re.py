# 영식이는 운동이나 휴식
# 운동 맥박 1분후 X+T
# 휴식 맥박 X-R
# 맥박 무조건 M이상
# M보다 높아지면 안되고 초기 맥박 m보다 낮아지면 안된다. 
# 운동 N분
# 5 70 120 25 15 운동 5분 맥박 70이상 120이하 25증가 15 감소

N, m, M, T, R = map(int, input().split())
pulse = m
time = 0
exercise = 0
while exercise < N:
    if m + T > M:
        break
    if pulse + T <= M:
        pulse += T
        exercise += 1
    elif pulse > M:
        break
    else:
        pulse -= R
        if pulse < m:
            pulse = m
    time += 1
print(time if exercise == N else -1)

# N, m, M, T, R = map(int, input().split())
# pulse = m
# h = 0
# while True:
#     if pulse - R < 0 or M - m < T or M - m < R:
#         h = -1
#         break
#     if pulse + T <= M:
#         pulse += T
#         N -= 1
#         h += 1
#         if N == 0:
#             break
#     elif pulse + T > M:
#         pulse -= R
#         h += 1
#     else:
#         h = -1
#         break
# print(h)
