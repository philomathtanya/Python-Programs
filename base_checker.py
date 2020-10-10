a = input()
b = input()
r = True
l1 = [0,1,2,3,4,5,6,7,8,9]
l2 = ['A', 'B', 'C', 'D', 'E', 'F']
l3 = ["Binary", "Octal", "Decimal", "Hex"]
for i in a:
    if i in l2:
        if b != l3[3]:
            r = False
            break
    elif int(i) in l1[8:10]:
        if b in l3[:2]:
            r = False
            break
    elif int(i) in l1[2:8]:
        if b == l3[0]:
            r = False
            break
    elif int(i) in l1[0:2]:
        if b not in l3:
            r = False
            break
print(r)

