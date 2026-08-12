import numpy as np
marks=np.array([[60,70,80],[70,80,90],[70,60,80]])
print(marks)
print(np.median(marks))
print(marks.shape)
result=np.median(marks,axis=0)
print(result)
result1=np.median(marks,axis=1)
print(result1)
