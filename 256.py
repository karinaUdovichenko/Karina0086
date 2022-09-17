x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
if x == x1 or y == y1:
    print("YES")
elif x - y == x1 - y1 or x + y == y1 + x1:
    print("YES")
else:
    print("NO")
