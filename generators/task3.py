import os
import random
import sys


LINE_TEMPLATE = '{:<4d}    {}'
IDS = [i for i in range(10)] * 100 + [i for i in range(10, 1000)]


random.seed(42)


def gen_factor():
    return random.random() * 2 + 0.5


try:
    while True:
        id_ = random.choice(IDS)
        print(LINE_TEMPLATE.format(id_, gen_factor()))

except (IOError, BrokenPipeError):
    sys.stdout = os.fdopen(1)
