#!/usr/bin/python

import sys
import time

last_day = None
f = None
for line in sys.stdin:
    ts = line.split()[0]

    ts = float(ts)

    day = time.strftime('%d', time.localtime(ts))

    if f is None or day != last_day:
        if f is not None:
            f.close()
        f = open(f'./data/session-{day}.out', 'w')

    f.write(line)
    last_day = day



