import random
from matplotlib import pyplot as plt

ls1 = [random.randrange(10, 100) for _ in range(10)]
ls2 = [random.randrange(0, 50) for _ in range(10)]
ls3 = [random.randrange(60, 200) for _ in range(10)]
xx = [x + 1 for x in range(10)]

plt.plot(xx, ls1, 'g-', label='ls1')
plt.plot(xx, ls2, 'r-.', label='ls2')
plt.plot(xx, ls3, 'b:', label='ls3')

plt.title('Multiline Chart')
plt.legend(loc=4)
plt.xlabel('Some value')
plt.xticks([])
plt.show()
