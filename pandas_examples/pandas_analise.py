import pandas as pd
import numpy as np

# Create a series with 100 random numbers
s = pd.Series(np.random.randn(4))
print(s)

print ("The axes are:")
print(s.axes)

print ("Is the Object empty?")
print(s.empty)

print ("The dimensions of the object:")
print(s.ndim)

print ("The size of the object:")
print(s.size)