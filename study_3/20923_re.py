import sys

from collections import deque
input = sys.stdin.readline
# sys.stdin = open('20923_input.txt')
c, turn = map(int, input().split())
dodeq = deque()
sudeq = deque()
for _ in range(c):
    d, s = map(int, input().split())
    dodeq.append(d)
    sudeq.append(s)
t = dc = sc = 0
do = deque()
su = deque()
for i in range(turn):
    if i % 2 == 0:
        dc = dodeq.pop()
        do.append(dc)
        if not dodeq:
            print('su')
            exit()
    else:
        sc = sudeq.pop()
        su.append(sc)
        if not sudeq:
            print('do')
            exit()
    if dc == 5 or sc == 5:
        dodeq.extendleft(su)
        dodeq.extendleft(do)
        su = deque()
        do = deque()
        dc = sc = 0
    elif dc and sc and dc + sc == 5:
        sudeq.extendleft(do)
        sudeq.extendleft(su)
        su = deque()
        do = deque()
        dc = sc = 0
if len(dodeq) > len(sudeq):
    print('do')
elif len(sudeq) > len(dodeq):
    print('su')
else:
    print('dosu')
