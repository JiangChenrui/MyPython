# -*- coding:utf-8 -*-

import time
import gevent

with gevent.Timeout(5, False):
    time.sleep(10)
    print 1
