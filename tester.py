import _thread
import time

def fxn(pauser):
    base_time = time.time()
    while True:
        for i in range(pauser):
            time.sleep(1)
        yield time.time()-base_time


gen = _thread.start_new_thread(fxn,(5,))

for i in range(10):
    time.sleep(6)
    print(next(gen))

print(el)
