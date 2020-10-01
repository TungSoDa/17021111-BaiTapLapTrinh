import math

def prob(n, p):
    return ((1-p)**(n-1))*p

def infoMeasure(n, p):
    return -math.log(prob(n, p), 2)

def sumP(N, p):
    # N = 1000 và p = 0.5 => mô phỏng việc tung đồng xu.
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p)
    return sum

def approxEntropy(N, p):
    # N = 1000, p = 0.5.
    sumHx = 0
    for i in range(1, N + 1):
        sumHx += prob(i, p) * infoMeasure(i, p)
    return sumHx

print(approxEntropy(1000, 0.5))
        