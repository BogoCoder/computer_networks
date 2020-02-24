import numpy.random


RTT = 5
pack_send = 0
t = 0

while t < 1000:
    len_bytes = np.random.geometric(p=0.35, size=10000)
