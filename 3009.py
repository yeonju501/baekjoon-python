rectangle = []
for T in range(3):
    rectangle.append(list(map(int, input().split())))
x = 0
if rectangle[0][0] == rectangle[1][0]:
    x = rectangle[2][0]
elif rectangle[0][0] == rectangle[2][0]:
    x = rectangle[1][0]
else:
    x = rectangle[0][0]
y = 0
if rectangle[0][1] == rectangle[1][1]:
    y = rectangle[2][1]
elif rectangle[0][1] == rectangle[2][1]:
    y = rectangle[1][1]
else:
    y = rectangle[0][1]
print(x, y)