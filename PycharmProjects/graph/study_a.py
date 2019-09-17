import matplotlib.pyplot as plt
import numpy as np

height1 = [80, 65, 100, 42, 54]  # 点数1
height2 = [55, 100, 98, 30, 21]  # 点数2

left = np.arange(len(height1))  # numpyで横軸を設定
labels = ['Japanese', 'Math', 'Science', 'Social', 'English']

width = 0.3

plt.bar(left, height1, color='r', width=width, align='center')
plt.bar(left + width, height2, color='b', width=width, align='center')

plt.xticks(left + width / 2, labels)
plt.show()