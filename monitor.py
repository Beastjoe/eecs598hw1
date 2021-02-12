import argparse
import time

import psutil

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--pid')

args = parser.parse_args()
pid = int(args.pid)

process = psutil.Process(pid)

start = time.time()
f = open("profile.txt", 'w')

while True:
    memory_usage = process.memory_info()[0] / 2. ** 30
    cpu_usage = process.cpu_percent()
    time_elapsed = time.time() - start
    f.write("{},{},{}\n".format(time_elapsed, cpu_usage, memory_usage))
    f.flush()
    time.sleep(1)