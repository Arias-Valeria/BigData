
import pandas as pd

import seaborn as sns

tarifas = pd.read_csv('tarifasEVF.csv')
df = pd.DataFrame(tarifas)
df.groupby('mes')['max_vol'].sum().plot(kind = 'bar', legend = 'Reverse')
