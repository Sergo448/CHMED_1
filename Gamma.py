# -*- coding: utf-8 -*-

from _g import gamma
from matplotlib import pyplot as plt

# Возврат значений из функции Func()
# object = class(*passing values to constructor*)
obj = gamma(gamma)

x, y = obj.funk()

# Строим график

fig, ax = plt.subplots()
ax.plot(x, y, color='red')

# Называем оси
plt.xlabel('Gamma from 0.1 to 2 with step 0.1')
plt.ylabel('Imaginary part of the resulting formula')

# Добавляем grid
ax.grid(color='black',
        linewidth=1,
        linestyle='dotted')
# Show
plt.show()
