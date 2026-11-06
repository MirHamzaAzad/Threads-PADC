# Parallel and Distributed Computing (PADC) - Threads & Synchronization

This repository demonstrates fundamental concepts of **Multithreading, Race Conditions, and Thread Synchronization** in Python using `threading.Thread` and `threading.Lock`.

---

## 📌 Overview

When multiple threads concurrently read, modify, and write back to a shared resource without coordination, unpredictable behavior and data corruption can occur—this is known as a **race condition**.

This project provides two distinct scenarios comparing un-synchronized execution against synchronized execution with locks:

1. **Scenario 1: Shared Joint Bank Account (Coarse-Grained Synchronization)**
   - `thread_no_lock.py`
   - `thread_with_lock.py`
2. **Scenario 2: Shared Receipt Generator & Parallel Processing (Fine-Grained Synchronization)**
   - `thread_2_no_lock.py`
   - `thread_2_with_lock.py`

---

## 📂 Project Structure

```text
.
├── thread_no_lock.py        # Bank account withdrawal simulation without locks (demonstrates race condition)
├── thread_with_lock.py      # Bank account withdrawal simulation with threading.Lock (thread-safe)
├── thread_2_no_lock.py      # Sequential receipt number generator without lock (race condition)
├── thread_2_with_lock.py    # Fine-grained lock for receipt generation while processing runs in parallel
└── README.md                # Documentation and analysis
```

---

## 🔍 Detailed Analysis & Execution Results

### Scenario 1: Joint Business Account Withdrawal

#### 1. Without Lock (`thread_no_lock.py`)
- **Shared Resource:** `balance = 10000`
- **Threads:**
  - Ali: withdraws Rs. 2,000 (takes 2 seconds)
  - Sara: withdraws Rs. 5,000 (takes 5 seconds)
  - Hamza: withdraws Rs. 3,000 (takes 3 seconds)
- **Problem:** All three threads read the initial balance concurrently as `10000`. Each performs subtraction based on stale data. The thread finishing last overwrites updates saved by prior threads.
- **Console Output:**
  ```text
  Ali   ne balance parha: Rs. 10000
  Sara  ne balance parha: Rs. 10000
  Hamza ne balance parha: Rs. 10000
  Ali   ne Rs. 2000 nikale, balance save kiya: Rs. 8000
  Hamza ne Rs. 3000 nikale, balance save kiya: Rs. 7000
  Sara  ne Rs. 5000 nikale, balance save kiya: Rs. 5000

  Starting balance : Rs. 10000
  Total withdrawn  : Rs. 10000
  Expected balance : Rs. 0
  Actual balance   : Rs. 5000
  --- 5.0 seconds ---
  ```
  *(Result: Inconsistent balance!)*

#### 2. With Lock (`thread_with_lock.py`)
- **Solution:** A mutex lock (`threading.Lock()`) protects the critical section (`read -> process -> write`).
- **Result:** Each thread acquires the lock before touching `balance` and releases it only after saving.
- **Console Output:**
  ```text
  Ali   ne balance parha: Rs. 10000
  Ali   ne Rs. 2000 nikale, balance save kiya: Rs. 8000
  Sara  ne balance parha: Rs. 8000
  Sara  ne Rs. 5000 nikale, balance save kiya: Rs. 3000
  Hamza ne balance parha: Rs. 3000
  Hamza ne Rs. 3000 nikale, balance save kiya: Rs. 0

  Starting balance : Rs. 10000
  Total withdrawn  : Rs. 10000
  Expected balance : Rs. 0
  Actual balance   : Rs. 0
  --- 10.0 seconds ---
  ```
  *(Result: Safe and deterministic!)*

---

### Scenario 2: Receipt Number Generator & Processing

#### 1. Without Lock (`thread_2_no_lock.py`)
- **Shared Resource:** `receipt_no = 0`
- **Problem:** Because threads read and increment `receipt_no` concurrently without synchronization, multiple threads receive identical receipt numbers.
- **Console Output:**
  ```text
  ---> Sara  shuru, Receipt No: 1
  ---> Ali   shuru, Receipt No: 1
  ---> Hamza shuru, Receipt No: 1
  ---> Ali   over, Receipt No: 1
  ---> Hamza over, Receipt No: 1
  ---> Sara  over, Receipt No: 1

  End
  Total receipts issue hui: 3, last receipt no: 1
  --- 5.1 seconds ---
  ```
  *(Result: Duplicate receipt numbers issued!)*

#### 2. With Fine-Grained Lock (`thread_2_with_lock.py`)
- **Solution:** Lock is acquired **only** during receipt number incrementation and released immediately. The long processing step (`time.sleep(self.duration)`) runs concurrently in parallel.
- **Console Output:**
  ```text
  ---> Ali   shuru, Receipt No: 1
  ---> Sara  shuru, Receipt No: 2
  ---> Hamza shuru, Receipt No: 3
  ---> Ali   over, Receipt No: 1
  ---> Hamza over, Receipt No: 3
  ---> Sara  over, Receipt No: 2

  End
  Total receipts issue hui: 3, last receipt no: 3
  --- 5.2 seconds ---
  ```
  *(Result: Unique sequential receipt numbers, while maintaining concurrent performance!)*

---

## 🚀 How to Run

Ensure Python 3.x is installed, then execute:

```bash
# Scenario 1
python thread_no_lock.py
python thread_with_lock.py

# Scenario 2
python thread_2_no_lock.py
python thread_2_with_lock.py
```

---

## 💡 Key Takeaways
- **Race Condition:** Occurs when thread execution interleaving leads to non-deterministic, buggy results.
- **Critical Section:** The section of code accessing shared mutable state.
- **Mutual Exclusion (`threading.Lock`):** Prevents multiple threads from entering the critical section concurrently.
- **Granularity Matters:** Keep critical sections as small as possible (fine-grained locking) to maximize concurrency and parallelism without sacrificing correctness.
