t, bs = open('input.txt')
bs = [*map(int, bs.replace('x','1').split(','))]

m, b = max((int(t)%b, b) for b in bs)
print((b-m) * b)

t, p = 0, 1
for i, b in enumerate(bs):
    while (t+i) % b: t += p
    p *= b

print(t)