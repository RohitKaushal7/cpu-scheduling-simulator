from src.utils.process import Process
import random

processes = []

for i in range(20):
    p = Process(i, random.randint(1, 50),
                random.randint(1, 50), random.randint(0, 5))
    processes.append(p)
