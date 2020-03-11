import numpy as np

class packet:
    def __init__(self,in_time,proc_time):
        self.in_time = in_time
        self.proc_time = proc_time

in_rate = 100
proc_rate = 200
num_packets = 100

is_queue = False
queue = []
total_queue_time = 0
current_time = 0

packets = []

for i in range(num_packets):
    packets.append(packet(np.random.exponential(1/in_rate), np.random.exponential(1/proc_rate)))

mean_proc_times = np.mean([p.proc_time for p in packets])
print(mean_proc_times)

for i in len(packets):
    packet = packets[i]
    current_time += packet.in_time
    if is_queue:
        pass
    else:
        pass
