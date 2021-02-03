import numpy as np 


class Compare:
    def __init__(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2
        #self.min_max_scaler = MinMaxScaler()
        
    def matrix(self, m1):
        return np.abs(m1[:, None] - m1)
    
    def dot(self):
        mat1 = self.matrix(self.seq1)
        mat2 = self.matrix(self.seq2)
        mat1 =  mat1.flatten()
        mat2 = mat2.flatten()
        return np.corrcoef(mat1, mat2)[0][1]
    
    def norm_dot(self):
        mat1 = self.matrix(self.seq1)
        mat2 = self.matrix(self.seq2)
        mat1 =  normalize(mat1.flatten())
        mat2 = normalize(mat2.flatten())
        return np.corrcoef(mat1, mat2)[0][1]
    
    def distance(self):
        mat1 = self.matrix(self.seq1)
        mat2 = self.matrix(self.seq2)
        mat1 =  mat1.flatten()
        mat2 = mat2.flatten()
        return np.abs(np.sum(mat1 - mat2))