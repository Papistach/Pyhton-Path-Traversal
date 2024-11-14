import random

random.seed(1)

password = ""

for i in range(30):
    password = password + chr(random.randint(33, 126))
    print(password)

print(password)
