prim = []

for i in range(1, 101):
    a = []
    for j in range(2, i):
        if i % j == 0:
            a.append(i)
    if not bool(a) :
        prim.append(i)

prim1 = set(prim)
print(prim1)