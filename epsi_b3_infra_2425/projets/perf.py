import random

l = []

for i in range(0, 100000):
    nb = random.randint(1111, 9999)
    l.append(nb)

print(l)