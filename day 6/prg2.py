import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
dot=np.dot(a,b)
print("dot:",dot)
ele=a*b
print("element:",ele)
print("a shape:",a.shape)
print("b shape:",b.shape)
print("dot shape:",dot.shape)
swap=np.dot(b,a)
print("swap:",swap)
print("swap shape:",swap.shape)