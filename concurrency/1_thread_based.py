# Thread based concurrency
# Thread run in the same process and share memory
# Good for I/O bound tasks ( eg downloading files , making API calls)
# Not ideal for CPU bound tasks due to Global Interpretor Lock (GIL)


import threading
import time

def worker(n):
    print(f"Worker {n} started")
    time.sleep(2) # simulate some work
    print(f"Worker {n} finished")
    
threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
    threads.append(t)
    
for t in threads:
    t.join()  # wait for all threads to finish

print("All workers completed")



# How it works
# Start 3 threads that execute concurrently
# Each thread sleeps for 2 seconds before finishing
# Since threads share memory they can easily communicate

