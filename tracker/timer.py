import time

'''
Split tracking
Total time
Pause/resume timer

Time accuracy
Time verifcation
Offline time tracking

from time import sleep
from random import randint

from timing import timer


t = timer()
t.startTimer()
for x in range(0, randint(10,99)):
    sleep(float(f'0.{randint(1,11)}'))
    t.addToBlocks()
    t.timeBlocks
'''

class timer(object):
    def __init__(self):
        self.resetTimer()

    def addToBlocks(self, start=False, blockType='split'):
        t = self.currentEpoch()
        if not start:
            n = self.currentTime(current=t)
            self.timeBlocks.append(n)
        else:
            self.timeBlocks.append(0)
        self.epochTimeBlocks.append(t)

    def removeFromBlocks(self):
        self.timeBlocks = self.timeBlocks[:-1]
        self.epochTimeBlocks = self.epochTimeBlocks[:-1]

    def currentEpoch(self):
        return time.time()

    def currentTime(self, current=None):
        if current is None:
            current = self.currentEpoch()
        t = current - self.lastTimeBlockEpoch()
        return t

    def currentElapsedTime(self):
        t1 = self.firstTimeBlock()
        if t1 is 0:
            return 0
        return self.currentEpoch() - t1

    def firstTimeBlock(self):
        if len(self.epochTimeBlocks) is 0:
            t = 0
        else:
            t = self.epochTimeBlocks[0]
        return t

    def lastTimeBlockEpoch(self):
        return self.epochTimeBlocks[-1]

    def lastTimeBlock(self):
        return self.timeBlocks[-1]

    def startTimer(self):
        self.resetTimer()
        t = self.currentEpoch()
        self.epochTimeBlocks.append(t)
        self.timeBlocks.append(0)

    def endTimer(self):
        self.addToBlocks()
        self.epochTimeBlocks = tuple(self.epochTimeBlocks)
        self.timeBlocks = tuple(self.timeBlocks)

    def resetTimer(self):
        self.epochTimeBlocks = []
        self.timeBlocks = []