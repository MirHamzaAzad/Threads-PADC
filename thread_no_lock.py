import time
from threading import Thread

# Shared resource: Joint Business Account
balance = 10000


class WithdrawThread(Thread):
    def __init__(self, name, amount, duration):
        Thread.__init__(self)
        self.name = name
        self.amount = amount
        self.duration = duration

    def run(self):
        global balance

        # Step 1: Balance parho
        current = balance
        print(self.name + " ne balance parha: Rs. " + str(current))

        # Step 2: Transaction process ho rahi hai (time lagta hai)
        time.sleep(self.duration)

        # Step 3: Naya balance save karo
        balance = current - self.amount
        print(self.name + " ne Rs. " + str(self.amount) +
              " nikale, balance save kiya: Rs. " + str(balance))


def main():
    start_time = time.time()

    # Thread Creation (name, amount, duration)
    ali = WithdrawThread("Ali  ", 2000, 2)
    sara = WithdrawThread("Sara ", 5000, 5)
    hamza = WithdrawThread("Hamza", 3000, 3)

    # Thread Running
    ali.start()
    sara.start()
    hamza.start()

    # Thread Joining
    ali.join()
    sara.join()
    hamza.join()

    print("\nStarting balance : Rs. 10000")
    print("Total withdrawn  : Rs. 10000")
    print("Expected balance : Rs. 0")
    print("Actual balance   : Rs. " + str(balance))
    print("--- %s seconds ---" % round(time.time() - start_time, 2))


if __name__ == "__main__":
    main()
