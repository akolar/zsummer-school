from datetime import datetime
import random
import sys


LINE_TEMPLATE = '{:%Y-%m-%dT%H:%M%:%S}   {}    {} {}'
NOW = datetime(2019, 7, 15, 15, 0, 0)


random.seed(42)

try:
    while True:
        class_ = random.randint(0, 1)
        print(LINE_TEMPLATE.format(NOW, class_, 'feature1=1', 'feature2=2'))
except IOError:
    sys.exit(0)
