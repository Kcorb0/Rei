import time
from multiprocessing import Process


def timer(length_seconds):
    count = 0

    while count != length_seconds:
        time.sleep(1)
        count += 1
        print(f"t: {count}")

    print(f"Your timer of {length_seconds}")


if __name__ == "__main__":
    t1 = 5
    t2 = 10

    Process(target=timer, args=(t1,)).start()
    Process(target=timer, args=(t2,)).start()
