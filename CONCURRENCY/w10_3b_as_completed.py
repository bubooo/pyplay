#!/usr/bin/env python3

'''
3b. Instead of waiting for all of the futures to complete, use "as_completed" to print the future results as they come available. Reuse your "ssh_command2" function to accomplish this. Once again use the concurrent futures "ThreadPoolExecutor" and print the "show version" results to standard output. Additionally, print the total execution time to standard output.
'''

# import modules
from concurrent.futures import ThreadPoolExecutor, as_completed
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
    pool = ThreadPoolExecutor(pool_size)
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
