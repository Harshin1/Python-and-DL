import numpy as np

a = np.random.randint(0,20,15)
print(a)
print(np.bincount(a).argmax())