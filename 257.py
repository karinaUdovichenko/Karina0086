x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
dx = abs(x - x1)
dy = abs(y - y1)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')
