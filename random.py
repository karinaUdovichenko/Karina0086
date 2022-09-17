import random
n = int(input())
x = random.randint(1,100)
k = 0
if n == x and k <= 10:
    k += 1
    print('вы победили')
while n < x:
    print('больше')
    k += 1
    n = int(input())
while n > x:
    print('меньше')
    k += 1 
    n = int(input())
if n != x and k > 10:
    print('вы проиграли')
    
