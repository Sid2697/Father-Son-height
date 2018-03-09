import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('Pearson.txt')
father_height = data[:, 0]
son_height = data[:, 1]
plt.scatter(father_height, son_height, s=9)
plt.xlabel("Father Height")
plt.ylabel("Son Height")
plt.title('Father_height VS. Son_height')
plt.show()
