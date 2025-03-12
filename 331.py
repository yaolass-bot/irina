import threading
import time

def thread_function(name):
    time.sleep(1)
    print(f"Thread {name}: finished")

if __name__ == "__main__":
    threads = []
    for i in range(5):
        thread = threading.Thread(target=thread_function, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All threads finished.")




