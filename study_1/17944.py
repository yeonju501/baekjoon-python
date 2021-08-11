n, t = map(int, input().split())
num_arm = n * 2
arm = 1
cnt = 1
while cnt < t:
    if cnt % ((num_arm*2)-2) >= num_arm or cnt % ((num_arm*2)-2) == 0:
        arm -= 1
        cnt += 1
    else:
        arm += 1
        cnt += 1
if t == 1:
    print(1)
else:
    print(arm)
#1 2 3 4 5 6 7 8 7 6 5 4 3 2 팔 갯수
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 나머지

#1 2 3 4 5 6 7 8 7 6 5 4 3 2 
#1 2 3 4 5 6 7 8 9 10 11 12 13 14