# multithreading = used to perform multiple tash concurrently (multitasking)
#       Good for I/O bound tasks ike reading files or fetching data from APIs
#       threading. Thread(target=my_function)

import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"you finish walking {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("you take out the trash")

def get_mail():
    time.sleep(4)
    print("you get the mail")

chore1 = threading.Thread(target=walk_dog, args=("scooby", "doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("all chores are complete")