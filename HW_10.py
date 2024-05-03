#  В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

# import pandas as pd
# import random

# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)

# data = pd.DataFrame({'whoAmI': lst})

# one_hot_encoded = pd.get_dummies(data, columns=['whoAmI'])

# print(one_hot_encoded.head())


import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
print(lst)
print()
data = pd.DataFrame({'whoAmI':lst})
data.loc[data['whoAmI'] == 'robot', 'r'] = '1'
data.loc[data['whoAmI'] != 'robot', 'r'] = '0'
data.loc[data['whoAmI'] == 'human', 'h'] = '1'
data.loc[data['whoAmI'] != 'human', 'h'] = '0'

data.head(n=11)



