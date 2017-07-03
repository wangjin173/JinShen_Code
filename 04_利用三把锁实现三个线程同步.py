#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from threading import Lock, Thread

import time

mutex_a = Lock()
mutex_b = Lock()
mutex_c = Lock()


def task_a():

    while True:

        # 申请锁a
        mutex_a.acquire()

        print("---------A---------")
        time.sleep(1)

        # 释放锁b
        mutex_b.release()


def task_b():

    while True:

        # 申请锁b
        mutex_b.acquire()

        print("---------B---------")
        time.sleep(1)

        # 释放锁c
        mutex_c.release()

def task_c():

    while True:

        # 申请锁c
        mutex_c.acquire()

        print("---------C---------")
        time.sleep(1)

        # 释放锁a
        mutex_a.release()

def main():

    # 让主线程获得锁b,锁c

    mutex_b.acquire()
    mutex_c.acquire()

    thread_a = Thread(target=task_a)
    thread_b = Thread(target=task_b)
    thread_c = Thread(target=task_c)

    thread_a.start()
    thread_b.start()
    thread_c.start()

    thread_a.join()
    thread_b.join()
    thread_c.join()


if __name__ == "__main__":
    main()