import numpy as np
import matplotlib.pylab as plt

# def step_function(x):
#     y = x > 0
#     return y.astype(np.int)
#
# x = np.arange(-5.0, 5.0, 0.1)
# y = step_function(x)
#
# plt.plot(x, y)
# plt.ylim(-0.1, 1.1) # 指定y轴范围
# plt.show()

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# x = np.arange(-5.0, 5.0, 0.1)
# y = sigmoid(x)
#
# plt.plot(x, y)
# plt.show()
