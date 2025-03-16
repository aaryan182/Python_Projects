# Process based concurrency ( multiprocessing )
# uses multiple processes each with its own memory space
# best for CPU bound tasks ( eg image processing , mathematical computations)
# Bypasses the GIL so true parallel execution is possible

import multiprocessing
import time

def worker(n):
    print(f"Process {n} started")
    time.sleep(2)
    print(f"Process {n} finished")

processes = []

for i in range(3):
    p = multiprocessing.Process(target=worker, args=(i,))
    p.start()
    processes.append(p)

for p in processes:
    p.join()  # wait for all processes to finish
    
print("All processes completed")


# How it works
# creates separate processes that run truly in parallel
# each process has its own memory space ( no shared variables )
# ideal for CPU heavy operations

