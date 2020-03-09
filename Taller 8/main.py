import numpy as np

in_rate = 100
proc_rate = 200
num_packets = 100

for packet in range(num_packets):
    in_time = np.random.exponential(1/in_rate)
    proc_time = np.random.exponential(1/proc_rate)
