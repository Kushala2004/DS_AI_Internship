import pandas as pd
data=pd.Series([10,'none',30,'none'])
print(data.isnull())
print(data.fillna(1))