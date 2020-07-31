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

from tracker import timer


t = timer(blocks=10)
t.startTimer()
for x in range(0, 9):
    sleep(float(f'{randint(1,11)}'))
    t.nextTimer()
    t.showElapsedBlocks()

'''

class timer(object):
    def __init__(self, blocks):
        self.allocateBlocks(n=blocks)

    def globalEpoch(self):
        return time.time()

    def currentAddBlock(self, nextTimer=False):
        t = self.globalEpoch()
        block = self.showActiveBlock()
        bn = self.showNextBlock()
        if len(self.blocks[block]) is 1:
            self.blocks[block].append(t)
        else:
            self.blocks[block] = [t]
        if nextTimer and bn is not None:
            self.blocks[bn] = [t]

    def currentDelBlock(self):
        bn = self.showActiveBlock()
        bp = self.showPreviousBlock()
        self.blocks[bn] = []
        if bp is not 0:
            self.blocks[bp] = [self.blocks[bp][0]]

    def allocateBlocks(self, n=None):
        if n is None:
            n = len(self.blocks.keys())
        self.blocks = dict(enumerate([[] for x in range(0,n)]))

    def showActiveBlock(self):
        for block, state in self.showActiveBlocks().items():
            if state:
                return block
        return 0

    def showActiveBlocks(self, n=1):
        i = {}
        for block in self.blocks.keys():
            i[block] = len(self.blocks[block]) is n
        return i

    def showCompletedBlocks(self):
        return self.showActiveBlocks(n=2)

    def showElapsedBlocks(self):
        i = {}
        for block in self.blocks.keys():
            if len(self.blocks[block]) is 2:
                i[block] = self.blocks[block][1] - self.blocks[block][0]
            else:
                i[block] = None
        return i

    def showElapsedTime(self):
        t = self.globalEpoch()
        return t - self.showStartTime()

    def showLastBlock(self):
        k = sorted(self.blocks.keys())[-1]
        return k

    def showNextBlock(self):
        block = self.showActiveBlock()
        if block + 1 is self.showLastBlock():
            return None
        return block + 1

    def showPreviousBlock(self):
        block = self.showActiveBlock()
        if block is 0:
            return 0
        return block - 1

    def showStartTime(self):
        block = self.showActiveBlock()
        if block is 0 and len(self.blocks[0]) is 0:
            return None
        else:
            return self.blocks[0][0]

    def currentTimer(self):
        return self.showElapsedTime()

    def startTimer(self):
        self.allocateBlocks()
        self.currentAddBlock()

    def nextTimer(self):
        self.currentAddBlock(nextTimer=True)

    def reverseTimer(self):
        self.currentDelBlock()