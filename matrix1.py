import numpy as np

def matrix_transform(sequence):
    "This function takes a sequence as input and transforms it into a square matrix by computing it combinatorial euclidean distances of each element of"
    entry = []
    abs_data = []
    for i in sequence:
        temp_list = []
        temp_list1 = []
        for v in sequence:
            temp_list.append(i-v)
        entry.append(temp_list)
        abs_data.append(np.abs(temp_list))
    return np.array(entry), np.array(abs_data)


def vector_transform(sequence):
    "This is similar to matrix transform but transforms the matrix into a vector"
    entry = []
    abs_data = []
    for i in sequence:
        temp_list = []
        temp_list1 = []
        for v in sequence:
            temp_list.append(i-v)
        entry.append(np.sum(temp_list))
        abs_data.append(np.sum(np.abs(temp_list)))
    return np.array(entry), np.array(abs_data)


def internal_energies(open1, high, low, close):
    "This function does a matrix transformation and outputs a figure as energy"
    "This function is highly correllated with STD"
    matrx = extractOHLC(open1=open1, high=high, low=low, close=close)
    sum1 = []
    mean1 = []
    for data in matrx:
        mat1 = matrix_transform(data)
        p1 = np.dot(mat1, data)
        sum1.append(np.sum(p1))
    return sum1

def extractOHLC(open1, high, low, close):
    "This function extracts open, high, low, close of a financial time series on the same level and outputs as a list"
    N = len(close)
    list_data = []
    for i in range(N):
        list_data.append([open1[i], high[i], low[i], close[i]])
    return list_data


def square_mat(seq):
    N = len(seq)
    root = int(np.sqrt(N))
    mat = []
    start = 0
    end = root
    for i in range(root):
        mat.append(seq[start:end])
        start += root
        end += root
    return np.array(mat)

def create_mat(seq):
    N = len(seq)
    mat = np.zeros((N,N))
    mat[0] = seq
    return mat