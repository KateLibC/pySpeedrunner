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
t.debug = True
t.startTimer()
for x in range(0, 9):
    sleep(float(f'{randint(1,11)}'))
    t.nextTimer()
    t.showElapsedBlocks()

from time import sleep
from random import randint

from tracker import timer


t = timer(blocks=10)
t.debug = True
t.startTimer()
for x in range(0, 8):
    sleep(0.1)
    t.nextTimer()
    t.showElapsedBlocks()

'''

class timer(object):
    def __init__(self, blocks):
        self.allocateBlocks(n=blocks)
        self.completed = False
        self.debug = False

    def globalEpoch(self):
        return time.time()

    def currentAddBlock(self, nextTimer=False):
        t = self.globalEpoch()
        block = self.showActiveBlock()
        bn = self.showNextBlock()
        if self.debug:
            print(f'Current epoch: {t}, Current block: {block}, Next block: {bn}')
        if len(self.blocks[block]) is 1:
            self.blocks[block].append(t)
            self.completed = block is self.showLastBlock()
            print(f'Adding to existing block: {block}, Completed: {self.completed}')
        else:
            self.blocks[block] = [t]
            print(f'Creating new block: {block}')
        if not self.completed:
            if nextTimer and bn is not None:
                self.blocks[bn] = [t]
                print(f'Creating new block via nextTimer: {block}')

    def currentDelBlock(self):
        if self.showNextBlock() is None:
            bn = self.showLastBlock()
            bl = bn - 1
            self.completed = False
        else:
            bn = self.showActiveBlock()
            bl = self.showPreviousBlock()
        bv = None
        if bn is not 0:
            self.blocks[bn] = []
            bv = self.blocks[bl][0]
            self.blocks[bl] = [bv]
        if self.debug:
            print(f'Block now: {bn}, Block last: {bl}, Completed: {self.completed}, New value: {bv}')

    def currentSkipBlock(self):
        block = self.showActiveBlock()
        if block is not None:
            bv = self.blocks[bv]
            self.blocks[block] = [bv, bv]
            self.completed = block is self.showLastBlock()

    def allocateBlocks(self, n=None):
        if n is None:
            n = len(self.blocks.keys())
        self.blocks = dict(enumerate([[] for x in range(0,n)]))

    def showActiveBlock(self):
        for block, state in self.showActiveBlocks().items():
            if state:
                return block
        if self.completed:
            return
        return 0

    def showActiveBlocks(self, n=1):
        i = {}
        for block in self.blocks.keys():
            i[block] = False
            if i[block] is not None:
                i[block] = len(self.blocks[block]) is n
        return i

    def showBlockCompleted(self):
        return len(self.blocks[self.showActiveBlock()]) is 2

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
        e = [y for x, y in self.showElapsedBlocks().items()]
        if None not in e:
            return sum(e)
        if self.showStartTime() is None:
            return 0
        return t - self.showStartTime()

    def showLastBlock(self):
        k = sorted(self.blocks.keys())[-1]
        return k

    def showNextBlock(self):
        if not self.completed:
            block = self.showActiveBlock()
            if block + 1 > self.showLastBlock():
                return
            elif block is self.showLastBlock():
                return self.showLastBlock()
            return block + 1
        return

    def showPreviousBlock(self):
        block = self.showActiveBlock()
        if block is 0:
            return 0
        elif block is None:
            return self.showLastBlock()
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
        self.completed = False

    def resetTimer(self):
        self.startTimer()

    def nextTimer(self):
        if not self.completed:
            self.currentAddBlock(nextTimer=True)

    def reverseTimer(self):
        self.currentDelBlock()