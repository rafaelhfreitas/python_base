#!/usr/bin/env python3


import os
import sys
import time
import logging

log = logging.Logger("errors")

def try_to_open_a_file(filepath, attempts=1) -> list:
    """Tries to open a file, if error, retries n times"""
    for attempt in range(1,attempts +1):
        try:
            return open(filepath).readlines()
        except FileNotFoundError as e:
            log.error("ERRO: %s",e)
            time.sleep(1)
        else:
            print("Success")
        finally:
            print("Execute this always")
    return []


for line in try_to_open_a_file("names.txt", attempts=5):
    print(line)

# try:    
#     print(names[1])
# except:
#     print("[Error] Missing name in the list")
#     sys.exit(1)