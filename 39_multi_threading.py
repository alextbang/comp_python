import threading
import time

def worker(num): #thread worker function
    """Thread worker function"""
    print(f'Thread {num} starting')
    time.sleep(2) # simulate some work being done
    print(f'Thread {num} finished')
    # the thread would take approximately 2 seconds to complete its work, so three threads would take approximately 6 seconds to complete their work if they were run sequentially. However, since they are run concurrently, the total time taken will be less than 6 seconds. In this case, the total time taken will be approximately 2 seconds, as all three threads will be running at the same time.

threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()  

for thread in threads:
    thread.join()  # wait for all threads to complete       

print('All threads have finished execution')