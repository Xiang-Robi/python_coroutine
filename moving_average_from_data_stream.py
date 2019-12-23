#!/usr/bin/env python3
#coding:utf-8

import time
import string
import random
import functools
import statistics
from collections import deque


def coroutine_primer(f):
    """A decorator that automatically primes the coroutine."""

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        coroutine = f(*args, **kwargs)
        next(coroutine)
        return coroutine
    return wrapper

def data_producer(digit_selector):
    """A char will be randomly selected from ascii_uppercase and digits."""

    pool = string.digits + string.ascii_uppercase
    i = 0
    while i < 20:
        data = random.choice(pool)
        digit_selector.send(data)
        time.sleep(random.uniform(0, 1))  # mimic the behavior of streaming data
        i += 1

@coroutine_primer
def digit_selector_coroutine(average_calculator, window_size=3):
    """Select digit from the data stream and update the moving window."""

    window = deque(maxlen=window_size)

    while True:
        raw_data = (yield)
        if raw_data.isdigit():
            window.append(int(raw_data))
            average_calculator.send(window)
        else:
            print('{} is not digit\n'.format(raw_data))

@coroutine_primer
def average_calculator_coroutine():
    """Calculate mean and output."""

    while True:
        window = (yield)
        print("current window = {}, mean = {:.3f}\n".format(list(window), statistics.mean(window)))


if __name__  == "__main__":

    calculator = average_calculator_coroutine()
    selector = digit_selector_coroutine(calculator, 3)
    data_producer(selector)
    
