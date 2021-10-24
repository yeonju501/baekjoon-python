
# 멀티탭 N 
# 멀티탭이 2 이상이면 멀티탭 한개를 꼽을 수 있다
# 3개면 2 + 다음 멀티탭 갯수
# 2개면 1 + 다음 멀티탭 갯수
# 1개면 컴퓨터 갯수
import sys
N = int(sys.stdin.readline())
hap = 0
for _ in range(N):
    hap += int(sys.stdin.readline())
print(hap-(N-1))
# 멀티탭 개수가 2 4 6 =  1 + 3 + 6
# 1 1 1 sum - (n-1)
