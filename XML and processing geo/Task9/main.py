x = input().split()
n = int(input())
x_n = float((float(x[2]) - float(x[0])) / n) # Широта
y_n = float((float(x[3]) - float(x[1])) / n) # Долгота

a = float(x[0])
b = float(x[1])
c = float(x[0])
d = float(x[1])
k = 0
for i in range(n):
    c += x_n
    d += y_n
    print(a, b, c, d)
    for j in range(n - 1):
        b += y_n
        d += y_n
        print(a, b, c, d)
    a += x_n
    b = float(x[1])
    d = float(x[1])