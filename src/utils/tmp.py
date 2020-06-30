from src.utils.process import Process
import random

processes = []

val = 7

# first process must arrive at time 0
processes.append(Process(0, 0, random.randint(1, val), random.randint(0, 3)))

for i in range(1, val):
    p = Process(i, random.randint(1, val),
                random.randint(1, val), random.randint(0, 3))
    processes.append(p)
