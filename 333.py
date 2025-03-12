

import time
import threading

def get_thread(thread_name):
    time.sleep(1)
    print(thread_name)

if __name__ == "__main__":
    thread1 = threading.Thread(target=get_thread, args=("Thread-1",))
    thread2 = threading.Thread(target=get_thread, args=("Thread-2",))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()





