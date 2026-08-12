import pandas as pd
x={"math":96,"science":87,"english":80}
y=pd.Series(x)
print(y)
print('science:',y['science'])
print(y[y>85])
print('english:',y['english'])