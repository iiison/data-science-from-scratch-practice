import random
from matplotlib import pyplot as plt

YEARS = [(x * 10) + 1950 for x in range(10)]
GDP = sorted([random.randrange(300, 14000) for _ in range(10)])
# GDP = [random.randrange(300, 14000) for _ in range(10)]

plt.plot(YEARS, GDP, color='orange', marker='*', linestyle='solid')
plt.title('GDP Line Graph')
plt.ylabel('GDP')
plt.xlabel('Years')
plt.show()
