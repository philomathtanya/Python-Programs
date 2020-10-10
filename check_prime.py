from math import sqrt
n = int(input())
r = "Prime"
for i in range(2, int(sqrt(n))+1):
    if n % i == 0:
        r = "Not Prime"
        break

print(r)
