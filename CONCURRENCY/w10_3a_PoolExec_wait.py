#!/usr/bin/env python3

'''
3a. Create a new function that is a duplicate of your "ssh_command" function. Name this function "ssh_command2". This function should eliminate all printing to standard output and should instead return the show command output. Note, in general, it is problematic to print in the child thread as you can get into race conditions between the threads. Using the "ThreadPoolExecutor" in Concurrent Futures execute "show version" on each of the devices defined in my_devices.py. Use the 'wait' method to ensure all of the futures have completed. Concurrent futures should be executing the ssh_command2 function in the child threads. Print the total execution time required to accomplish this task.
'''

# import modules
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
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

    # wait till all futures/threads get completed
    wait(threads)

    for thread in threads:
        print("=-"*30)
        print("Result:\n{}".format(thread.result()))
        print("\n\n")
    print("Elapsed time: {}".format(time.time() - start_time))
# THE CODE

if __name__ == "__main__":
    main()
