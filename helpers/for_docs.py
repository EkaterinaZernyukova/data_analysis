import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
print(mpl.__version__)

x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.show()
