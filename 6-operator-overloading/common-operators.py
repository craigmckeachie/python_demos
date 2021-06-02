print(3 * 2)

print([1, 2, 3] * 2)

# pip3 install numpy pandas

import numpy as np


print(np.array([1,2,3]) * 2)

import pandas as pd

food = pd.Series({
    'apples': 2,
    'oranges': 4,
    'grapes': 6
})

print(food * 2)

items = pd.DataFrame({
 'qty':pd.Series({
    'apples': 2,
    'oranges': 4,
    'grapes': 6
   }),
  'amt': pd.Series({
    'apples': 1.49,
    'oranges': .99,
    'grapes': 2.49
   })
})

print( items * 2)

print('1,2,3 ' * 2)
# print('1,2,3' * '2') # errors



