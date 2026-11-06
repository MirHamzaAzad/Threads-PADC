import threading
import time
from threading import Thread

# Shared resource: Receipt number generator
receipt_no = 0

# Lock Definition
threadLock = threading.Lock()


class TransactionThread(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        global receipt_no

        # Part 1: Receipt number lena (SHARED, isliye lock)
        threadLock.acquire()
        current = receipt_no
        time.sleep(0.1)              # same gap, lekin ab lock ki wajah se safe
        receipt_no = current + 1
        my_receipt = receipt_no
        threadLock.release()         # kaam khatam, foran lock chhor do

        print("---> " + self.name + " shuru, Receipt No: " + str(my_receipt))

        # Part 2: Transaction processing (lock ke BAHAR, sab parallel)
        time.sleep(self.duration)
        print("---> " + self.name + " over, Receipt No: " + str(my_receipt))


def main():
    start_time = time.time()

    # Thread Creation (name, duration)
    ali = TransactionThread("Ali  ", 2)
    sara = TransactionThread("Sara ", 5)
    hamza = TransactionThread("Hamza", 3)

    # Thread Running
    ali.start()
    sara.start()
    hamza.start()

    # Thread Joining
    ali.join()
    sara.join()
    hamza.join()

    print("\nEnd")
    print("Total receipts issue hui: 3, last receipt no: " + str(receipt_no))
    print("--- %s seconds ---" % round(time.time() - start_time, 2))


if __name__ == "__main__":
    main()
