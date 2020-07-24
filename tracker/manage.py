import json
import time
import os
import hashlib

from .timer import timer

'''
from tracker import manage
f = 'LegendofIllusionStarringMickeyMouse.Any.pysplit'
m = manage(splitFile=f)
m.loadSplitData()
m.splitData

'''

class manage(object):
    def __init__(self, gameTitle=None, gameCategory='Beat the Game', platform=None, splitFile=None):
        self.gameTitle = gameTitle
        self.gameCategory = gameCategory
        self.platform = platform
        self.splitFile = splitFile
        self.splitDirectory = './'
        self.splitData = None

    def defaultSplitData(self):
        t = time.time()
        return {
            'GameTitle': self.gameTitle,
            'GameCategory': self.gameCategory,
            'Platform': self.platform,
            'Meta': {
                'Created': t,
                'Updated': t,
            },
            'SplitReference': {},
            'Events': {},
        }

    def createNewSplit(self, name):
        if len(self.splitData['SplitReference'].keys()) is 0:
            n = 0
        else:
            n = sorted(self.splitData['SplitReference'].keys())[-1] + 1
        x = f'{name}.{n}'.encode('utf-8')
        i = {'Title': name, 'ObjectID': hashlib.sha256(x).hexdigest(), 'Status': 0}
        self.splitData['SplitReference'][n] = i

    def createNewSession(self):
        s = {
            'SessionStart': time.time(),
            'SessionEnd': None,
            'SessionData': []
        }
        sid = self.createNewSessionID()
        self.splitData['SplitReference'][sid] = s

    def createNewSessionID(self):
        n = 0
        if len(self.splitData['SplitReference'].keys()) is not 0:
            n = sorted(self.splitData['SplitReference'].keys())[:-1] + 1
        return n

    def metaUpdate(self):
        self.splitData['Meta']['Updated'] = time.time()

    def loadSplitData(self):
        self.splitData = self.defaultSplitData()
        if self.splitFile is not None:
            if os.path.exists(os.path.join(self.splitDirectory, self.splitFile)):
                with open(os.path.join(self.splitDirectory, self.splitFile), 'r') as f:
                    self.splitData = json.load(f)
        self.gameTitle = self.splitData['GameTitle']
        self.gameCategory = self.splitData['GameCategory']
        self.platform = self.splitData['Platform']

    def saveSplitData(self):
        self.metaUpdate()
        def safeFile(char):
            return False not in [char.isdigit() or char.isalpha() or char in '._-']
        fn = ''.join([x for x in f'{self.gameTitle}.{self.gameCategory}' if safeFile(x)])
        fn = f'{fn}.pysplit'
        p = os.path.join(self.splitDirectory, fn)
        with open(p, 'w') as f:
            f.write(json.dumps(self.splitData, indent=2))