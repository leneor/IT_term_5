import math
import numpy as np
y = [math.e/(math.log(2)+9), math.e/(math.log(2)+9)]
result = open("file.txt", "w")
result.write('N=0' + ' ' +str(y[1])+ '\n')
result.write('N=1' + ' ' +str(y[1])+ '\n')

for N in range(2,100):
    y.append((math.e - 10 * y[N - 1] + y[N - 2]) / math.log(2))
    x = y[N]
    result.write('N=' + str(N) + ' ' +str(x))
    result.write('\n')


