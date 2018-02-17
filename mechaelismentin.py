import heapq as hp
import Queue as que
import numpy as np

class Estruct:
    def __init__(self, etype, time):
        self.etype = etype
        self.etime = time

class Enzyme:
    def __init__(self):
        self.allosites = 1
        self.servicerate = 0

class Clock:
    def __init__(self):
        self.time = 0
        self.lastevent = 0

class Environment:

    def __init__(self, substrate, product, volume):
        self.substrate = 0
        self.product = 0
        self.volume = 0
        self.clock = 0
        self.es = None
        self.ep = None
        self.cal = []

    def clockacc(self, timeadd):
        self.clock += timeadd

    def createEs(self):
        es = Enzyme()
        self.es = es

    def createEp(self):
        ep = Enzyme()
        self.ep = ep

    def initializeEnvironment(self):
        self.createEp()
        self.createEs()

    def updateClock(self):
        event = hp.heappop(self.cal)
        self.clockacc(event.etime)

    def runSim(self):
        self.initializeEnvironment()
        i = 0
        first = Estruct(0, np.random.exponential(1))
        hp.heappush(self.cal, first)
        while (i<10):
            hp.heappush(self.cal, first)
            self.updateClock()
            print self.clock
            i+=1

env = Environment(100,100,1000)
env.runSim()
