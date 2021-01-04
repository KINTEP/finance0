import numpy as np 


def sinefit(data):
    N = len(data)
    fit = np.zeros(N)
    time = np.array([i for i in range(1, N+1)])
    corr = np.corrcoef(data, fit)[1][0]
    counter = 1
    while corr != 1:
        corr = np.corrcoef(data, fit)[1][0]
        sin = np.sin(counter*time)
        coef = np.dot(sin, data)
        fit += coef * sin
        counter += 1
    return fit

