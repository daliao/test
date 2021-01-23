# -*- coding: utf-8  -*-
#!/usr/local/bin/python
import time, timeit


def test_fun():
    BUSYTIME = 10
    IDLETIME = 10
    while True:
        startTime = time.time()
        while (time.time() - startTime) * 1000 < BUSYTIME:
            pass
        time.sleep(IDLETIME)

if __name__=="__main__":
    print(timeit.timeit("test_fun()", setup="from __main__ import test_fun", number=1))
