import sys
sys.stdin = open('20006_input.txt')

p, m = map(int, input().split())
person = [input().split() for _ in range(p)]
for i in range(p):
    person[i][0] = int(person[i][0])
room = [[person[0]]]

for i in range(1, p):
    for j in range(len(room)):
        level = room[j][0][0]
        if (level - 10) <= person[i][0] <= (level + 10) and len(room[j]) < m:
            room[j].append(person[i])
            break
    else:
        room.append([person[i]])

for i in range(len(room)):
    room[i].sort(key=lambda x: x[1])

for i in range(len(room)):
    if len(room[i]) == m:
        print('Started!')
    else:
        print('Waiting!')
    for j in range(len(room[i])):
        print(room[i][j][0], room[i][j][1])


