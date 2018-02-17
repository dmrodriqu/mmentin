import heapq as hp
import Queue
import numpy as np

class Estruct:
    def __init__(self, etype, time):
        self.etype = etype
        self.etime = time

class Enzyme:
    def __init__(self):
        self.allosites = 1
        self.servicerate = 0
        self.busy = False
        self.queue = None
        self.initializeEnzyme()

    def initializeEnzyme(self):
        q = Queue.Queue(maxsize = 1)
        self.queue = q

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
        print event.etype
        print event.etime
        return event.etype

    def scheduleEvent(self, etype):
        curtime = self.clock
        arrtime = curtime + np.random.exponential(1)
        event = Estruct(etype,arrtime)
        return event


    def handleArrival(self):
        aevent = self.scheduleEvent(0)
        hp.heappush(self.cal, aevent)
        if (self.es.busy == True):
            # mutual exclusion
            self.es.queue.put(aevent)
            if (Queue.Full(self.es.queue)):
                print "no!"
            self.ep.busy = False
        if (self.ep.busy == False):
            # mutual exclusion
            self.es.busy = True
            self.ep.busy = True
            # set delay to 0
            # add 1 to number of delayed
            # make busy
            # schedule departure
            devent = self.scheduleEvent(1)
            hp.heappush(self.cal, devent)

    def handleDeparture(self):
        # queue empty
            #
        # queue non empty
            # subtract 1 from queue
            # compute delay
            # add 1 to # of delay
            # schedule departure
            devent = self.scheduleEvent(1)
            hp.heappush(self.cal, devent)

    def handleEstoEp(self):
        self.substrate -= 1

    def handleEptoEs(self):
        self.product -= 1


    def runSim(self):
        self.initializeEnvironment()
        i = 0
        first = Estruct(0, np.random.exponential(1))
        hp.heappush(self.cal, first)
        while (i<10):
            mtype = self.updateClock()
            # substrate or product
            if(mtype == 0):
                # handle arrival
                self.handleArrival()
                # handle departure
            # es to ep
            if(mtype == 1):
                # handle arrival
                self.handleDeparture()
                # handle departure

            # ep to es
            i+=1

env = Environment(100,0,1000)
env.runSim()
