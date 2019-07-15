from datetime import datetime
import json
import os
import random
import sys


LINE_TEMPLATE = '{:%Y-%m-%dT%H:%M%:%S}   {}    {} {}'
NOW = datetime(2019, 7, 15, 15, 0, 0)


random.seed(42)

try:
    i = 0
    while True:
        class_ = random.randint(0, 12)

        j = {
            'class': class_,
            'now': NOW.isoformat(),
            'id': i,
            'feature1': 100,
            'feature2': 200,
        }
        print(json.dumps(j), flush=True)

        i += 1

except (IOError, BrokenPipeError):
    sys.stdout = os.fdopen(1)
