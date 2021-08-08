# 1/1 : 1
# 1/2 2/1 : 2
# 3/1 2/2 1/3 :3
# 1/4 2/3 3/2 4/1 :4
# 5/1 4/2 3/3 2/4 1/5 :5
# 전체 갯수 n-1
import sys
x = int(sys.stdin.readline().strip())
hap = 0
n = 1
while hap+n < x:
    hap += n
    n += 1 
# hap 10 n 5
remainder = x-hap #4
if n%2:
    print(f'{n-remainder+1}/{remainder}')
else:
    print(f'{remainder}/{n-remainder+1}')

    

