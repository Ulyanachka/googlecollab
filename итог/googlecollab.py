import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
print(lst)
print()
data = pd.DataFrame({'whoAmI':lst})
data.loc[data['whoAmI'] == 'robot', 'group'] = '1'
data.loc[data['whoAmI'] != 'robot', 'group'] = '0' # -
data.loc[data['whoAmI'] == 'human', 'group'] = '1'
data.loc[data['whoAmI'] != 'human', 'group'] = '0' # -

data.head(n=20) 