n = int(input("Enter a number: "))
a = 0
b = 1
if n == 0:
    print(a)
else:
    c = a+b
    print(a)
    print(b)
    while c <= n:
        print(c)
        a = b
        b = c
        c = a + b
