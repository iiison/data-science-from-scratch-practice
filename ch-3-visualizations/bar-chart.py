import random
from matplotlib import pyplot as plt

MOVIES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
VIEWERS = [random.randrange(3, 50) for _ in range(10)]

plt.bar(MOVIES, VIEWERS)
plt.title('Movies and Viewers Chart')
plt.ylabel('# of Viewers in Million')

plt.show()
