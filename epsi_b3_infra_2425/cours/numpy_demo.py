import numpy as np

# import random


# l = []
# for i in range(10000):
#     l2 = []
#     for j in range(10000):
#         l2.append(random.randint(0, 99))
#     l.append(l2)

# print(np.array(l))

# arr_rnd = np.random.randint(0, 99, (10000, 10000))
# arr_rnd = arr_rnd ** 9
# print(arr_rnd[-1:, -3:])

import matplotlib.pyplot as plt

image = np.random.rand(1080, 1920, 3)
print((image * 255).round())

plt.imshow(image)
plt.show()

