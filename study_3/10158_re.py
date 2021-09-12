
# 가로 W 세로 h
import sys
sys.stdin = open('10158_input.txt')
# input = sys.stdin.readline
w, h = map(int, input().split()) # 6 4
p, q = map(int, input().split()) # 5 3
t = int(input())
p += t
q += t
p %= (2*w)
q %= (2*h)
if p > w:
    p = 2 * w -p
if q > h:
    q = 2 * h - q
print(p, q)






