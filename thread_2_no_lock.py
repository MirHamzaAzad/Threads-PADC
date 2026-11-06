import time
from threading import Thread

# Shared resource: Receipt number generator
receipt_no = 0


class TransactionThread(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        global receipt_no

        # Part 1: Receipt number lena (SHARED, bina lock ke)
        current = receipt_no
        time.sleep(0.1)              # chhota sa gap jahan race condition hoti hai
        receipt_no = current + 1
        my_receipt = receipt_no
        print("---> " + self.name + " shuru, Receipt No: " + str(my_receipt))

        # Part 2: Transaction processing (apna alag kaam)
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
