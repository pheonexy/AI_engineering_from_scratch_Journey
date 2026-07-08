# proj_b(a) = (a dot b / b dot b ) * b
# dot : dot product => a dot b = a1*b1 + a2*b2 + ..
import numpy as np
def proj(vector,vector_):
    # multiplication of a scalar(x) and a vector(y)
    def multiplify(x,vector):
        vector_ = []
        for i in vector:
            vector_.append(x*i)
        return vector_
    r = np.dot(vector,vector_) / np.dot(vector_,vector_)
    print(multiplify(r,vector_))

# a=[3,4], b= [1,0] => proj(a,b) => [3.0, 0.0]
