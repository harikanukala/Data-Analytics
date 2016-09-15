import numpy as np
def p(x,coeff):
    A=np.empty(len(coeff))
    A[0]=1
    A[1:]=x
    y=np.cumprod(A)
    print np.sum(coeff*y)

p(2,[2,3,4])