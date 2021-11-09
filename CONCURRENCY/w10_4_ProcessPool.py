#!/usr/bin/env python3

'''
Create a new program that completes the same task as Exercise 3b except using multiple processes (i.e. a 'ProcessPoolExecutor').
'''

# import modules
from concurrent.futures import ProcessPoolExecutor, as_completed
from my_devices import my_devices
from my_functions import ssh_command2
import time


# define CONSTANTS

# define variable intial values
pool_size = 4
threads = []

# define functions

def main():
    start_time = time.time()
    pool = ProcessPoolExecutor(pool_size)
    for device in my_devices:
        thread = pool.submit(ssh_command2, device, "show version")
        threads.append(thread)

    # process completed threads

    for thread in as_completed(threads):
        print("=-"*30)
        print("Result:\n{}".format(thread.result()))
        print("\n\n")
    print("Elapsed time: {}".format(time.time() - start_time))
# THE CODE

if __name__ == "__main__":
    main()
