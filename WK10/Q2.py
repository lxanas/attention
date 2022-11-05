import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 9, 100)
y = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y, label='Sine')
plt.plot(x, y2, label='Cosine')

plt.xlabel('x axis label')
plt.ylabel('y axis label')

plt.title("Sine and Cosine")

plt.legend()

plt.show()
