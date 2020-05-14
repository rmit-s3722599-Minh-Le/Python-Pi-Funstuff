

class Customer:
    def __init__(self, queue_num, name):
        self.missed_call = 0
        self.queue_num = queue_num
        self.name = name

    def getQueue(self):
        return self.queue_num

    def decrQueue(self):
        self.queue_num -= self.queue_num
    def getName(self):
        return self.name
    def incrmiss(self):
        self.missed_call += 1
    def getMissedCalls(self):
        return self.missed_call
    def resetMissedCalls(self):
        self.missed_call = 0
    def toString(self):
        print("---------------------------")
        print("Queue num: {}".format(self.queue_num))
        print("Name: {}".format(self.name))
        print("Missed Calls: {}".format(self.missed_call))
        print("---------------------------")
    