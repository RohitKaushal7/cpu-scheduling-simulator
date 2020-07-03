from src.utils.process import Process
import random

processes = []

n = 7
burst = 10
priority = 5

# first process must arrive at time 0
processes.append(Process(0, 0, random.randint(
    1, burst), random.randint(1, priority)))

for i in range(1, n):
    p = Process(i, random.randint(1, n),
                random.randint(1, burst), random.randint(1, priority))
    processes.append(p)
