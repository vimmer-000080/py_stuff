import matplotlib.pyplot as plt
import numpy as np
vectors = np.array([complex(1,2), complex(2,-3)])
plt.quiver(np.real(vectors), np.imag(vectors), angles='xy', scale_units='xy', scale=1)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()
