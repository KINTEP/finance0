def detrend(sequence):
    "This takes a sequence and outputs the difference between two successive elements"
    diffs = [0]
    for i in range(1, len(sequence)):
        prev = i - 1
        now = i
        diffs.append(sequence[prev] - sequence[now])
    return diffs

def normalize(sequence):
    max1 = np.max(sequence)
    min1 = np.min(sequence)
    data = []
    for val in sequence:
        norm = (val - min1)/(max1 - min1)
        data.append(norm)
    return data


def lags(n, data):
    "This function takes in sequence and outputs the lag periods as a matrix"
    all_data = []
    N = len(data)
    start = n-1
    for i in range(n):
        ls = data[start:N-i]
        all_data.append(ls)
        start -= 1
    return all_data

def extractOHLC(open1, high, low, close):
    "This function extracts open, high, low, close of a financial time series on the same level and outputs as a list"
    N = len(close)
    list_data = []
    for i in range(N):
        list_data.append([open1[i], high[i], low[i], close[i]])
    return list_data