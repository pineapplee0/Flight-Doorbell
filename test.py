#!/usr/bin/env python3
import time
import random
import math

ids = [ "A349BE", "A63BF4", "A46E8D", "A63FB3", "AB3645", "A663BF", "AB3445", "A345BF" ]

def rand(maxnum):
    return(round(random.random() * maxnum))

for i in range(1,1000):
    print("MSG,3,,,{},,,,,,,{},,,30.{},-97.{},,,0,0,0,0".format(ids[rand(len(ids)-1)], rand(20000), rand(99999), rand(99999)))
    time.sleep(2)
