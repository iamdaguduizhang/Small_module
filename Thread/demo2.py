import threading


count = 0


def run_thread(lock):
    global count
    for i in range(10000):
        with lock:
            count += 1
        lock.release


# t1 = threading.Thread(target=run_thread,args=())
# t2 = threading.Thread(target=run_thread,args=())
# t1.start()
# t2.start()
# t1.join()
# t2.join()


lock = threading.Lock()
threads = []
for i in range(2):
    t = threading.Thread(target=run_thread, args=(lock, ))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()
print(count)
