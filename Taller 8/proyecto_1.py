import numpy as np

class packet:
    def __init__(self,in_time,proc_time):
        self.in_time = in_time
        self.proc_time = proc_time

def increase_time(packet_index, t):
    global packets
    global num_packets
    global current_time
    global start_queue
    global queue
    original_t = t
    for i in range(packet_index+1, num_packets):
        if packets[i].in_time < t:
            queue.append(i)
            if start_queue == 0: start_queue = current_time + packets[i].in_time
            t -= packets[i].in_time
            packets[i].in_time = 0
        else:
            packets[i].in_time -= t
            break
    current_time += original_t

def simulation(in_rate, proc_rate):
    global packets
    global num_packets
    global start_queue
    global current_time
    total_queue_time = 0
    for i in range(num_packets):
        packets.append(packet(np.random.exponential(1/in_rate), np.random.exponential(1/proc_rate)))
    mean_proc_times = np.mean([p.proc_time for p in packets])
    for i in range(num_packets):
        current_time += packets[i].in_time
        if i in queue:
            queue.remove(i)
            if len(queue) == 0:
                total_queue_time = total_queue_time + current_time - start_queue
                start_queue = 0
        increase_time(i, packets[i].proc_time)
    mean_queue_time = total_queue_time/num_packets
    return mean_proc_times, mean_queue_time

num_packets = num_simulations = 100
z = 1.96

current_time = start_queue = 0
packets = []
queue = []

in_rate = 100
proc_rate = 200
proc_times = []
queue_times = []
total_times = []
for sim in range(num_simulations):
    proc_time, queue_time = simulation(in_rate, proc_rate)
    proc_times.append(proc_time)
    queue_times.append(queue_time)
    total_times.append(current_time)
    current_time = start_queue = 0
    packets = []
    queue = []

mean_proc_times_interval = [np.mean(proc_times)-z*np.std(proc_times)/np.sqrt(num_simulations), np.mean(proc_times)+z*np.std(proc_times)/np.sqrt(num_simulations)]
mean_queue_times_interval = [np.mean(queue_times)-z*np.std(queue_times)/np.sqrt(num_simulations), np.mean(queue_times)+z*np.std(queue_times)/np.sqrt(num_simulations)]
total_times_interval = [np.mean(total_times)-z*np.std(total_times)/np.sqrt(num_simulations), np.mean(total_times)+z*np.std(total_times)/np.sqrt(num_simulations)]

print('Tasa de arribos =', in_rate, ', tasa de procesamiento = ', proc_rate, ', nivel de confianza = 95%')
print('Intervalo de confianza para tiempo promedio de procesamiento:', mean_proc_times_interval)
print('Intervalo de confianza para tiempo promedio en cola:', mean_queue_times_interval)
print('Intervalo de confianza para tiempo total:', total_times_interval, '\n')

in_rate = 150
proc_rate = 200
proc_times = []
queue_times = []
total_times = []
for sim in range(num_simulations):
    proc_time, queue_time = simulation(in_rate, proc_rate)
    proc_times.append(proc_time)
    queue_times.append(queue_time)
    total_times.append(current_time)
    current_time = start_queue = 0
    packets = []
    queue = []

mean_proc_times_interval = [np.mean(proc_times)-z*np.std(proc_times)/np.sqrt(num_simulations), np.mean(proc_times)+z*np.std(proc_times)/np.sqrt(num_simulations)]
mean_queue_times_interval = [np.mean(queue_times)-z*np.std(queue_times)/np.sqrt(num_simulations), np.mean(queue_times)+z*np.std(queue_times)/np.sqrt(num_simulations)]
total_times_interval = [np.mean(total_times)-z*np.std(total_times)/np.sqrt(num_simulations), np.mean(total_times)+z*np.std(total_times)/np.sqrt(num_simulations)]

print('Tasa de arribos =', in_rate, ', tasa de procesamiento = ', proc_rate, ', nivel de confianza = 95%')
print('Intervalo de confianza para tiempo promedio de procesamiento:', mean_proc_times_interval)
print('Intervalo de confianza para tiempo promedio en cola:', mean_queue_times_interval)
print('Intervalo de confianza para tiempo total:', total_times_interval, '\n')

in_rate = 50
proc_rate = 200
proc_times = []
queue_times = []
total_times = []
for sim in range(num_simulations):
    proc_time, queue_time = simulation(in_rate, proc_rate)
    proc_times.append(proc_time)
    queue_times.append(queue_time)
    total_times.append(current_time)
    current_time = start_queue = 0
    packets = []
    queue = []

mean_proc_times_interval = [np.mean(proc_times)-z*np.std(proc_times)/np.sqrt(num_simulations), np.mean(proc_times)+z*np.std(proc_times)/np.sqrt(num_simulations)]
mean_queue_times_interval = [np.mean(queue_times)-z*np.std(queue_times)/np.sqrt(num_simulations), np.mean(queue_times)+z*np.std(queue_times)/np.sqrt(num_simulations)]
total_times_interval = [np.mean(total_times)-z*np.std(total_times)/np.sqrt(num_simulations), np.mean(total_times)+z*np.std(total_times)/np.sqrt(num_simulations)]

print('Tasa de arribos =', in_rate, ', tasa de procesamiento = ', proc_rate, ', nivel de confianza = 95%')
print('Intervalo de confianza para tiempo promedio de procesamiento:', mean_proc_times_interval)
print('Intervalo de confianza para tiempo promedio en cola:', mean_queue_times_interval)
print('Intervalo de confianza para tiempo total:', total_times_interval, '\n')