import matplotlib.pyplot as plt
import numpy as np

for i in range(3):
    plt.plot(np.arange(10) + i)

cm = plt.get_cmap('prism')
print cm(1), cm(2), cm(3)
NPOINTS = 3
plt.gca().set_color_cycle([cm(1.*i/(NPOINTS-1)) for i in range(NPOINTS-1)])

for i in range(3):
    plt.plot(np.arange(10, 1, -1) + i)

plt.show()
