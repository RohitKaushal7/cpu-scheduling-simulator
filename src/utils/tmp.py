from src.utils.process import Process
import random

processes = []

# first process must arrive at time 0
processes.append(Process(0, 0, random.randint(1, 5), random.randint(0, 5)))

for i in range(1, 5):
    p = Process(i, random.randint(1, 5),
                random.randint(1, 5), random.randint(0, 5))
    processes.append(p)
