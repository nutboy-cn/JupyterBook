print(123)
import numpy as np

def naive_vector_dot(x.y):
    assert len(x.shape)==1
    assert len(y.shape)==1
    assert x.shape[0]==y.shape[0]
    z=0
    for i in range(x.shape[0]):
        z+=x[i]*y[i]
    return z
def navie_matrix_vector_dot(x,y):
    assert len(x.shape)==2
    assert len(y.shape)==1
    assert x.shape[1]==y.shape[0]

    z=np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            z[i]+=x[i,j]*y[j]
    return z

