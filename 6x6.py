import matplotlib.pyplot as plt
import numpy as np

pat = np.matrix([0,0,1,1,1,1, 0,0,1,0,0,0, 0,0,1,1,1,1, 0,0,1,0,0,1, 0,0,1,1,1,1, 0,0,0,0,0,0])
pat = np.matrix.reshape(pat,6,6)
print(pat)

plt.figure(1)
plt.imshow(pat)
plt.show()