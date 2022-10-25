import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots(1, 2)
plt.plot(1, np.cos(1))

plt.subplots(1, 2)
plt.plot(1, np.sin(1))

plt.title("Sin and cos")

plt.show()
