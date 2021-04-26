from random import randint
from datetime import datetime
import uuid

class FlashCardEntry:

    def __init__(self,
                 userID = "user-"+str(uuid.uuid4()),
                 sessionID = "session-"+str(uuid.uuid4()),
                 entryID = "entry-"+str(uuid.uuid4()),
                 date=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                 patternID = randint(0, 10),
                 result = 1,
                 responseTime = randint(1, 500)):

        self.userID = userID
        self.sessionID = sessionID
        self.entryID = entryID
        self.date = date
        self.patternID = patternID
        self.result = result
        self.responseTime = responseTime

    def getEntryDict(self):
        return {
                "userID"        : self.userID,
                "sessionID"     : self.sessionID,
                "entryID"       : self.entryID,
                "date"          : self.date,
                "patternID"     : self.patternID,
                "result"        : self.result,
                "responseTime"  : self.responseTime
        }

    def printEntry(self):
        print("{:<12} {:1} {:<36}".format("userID", "=", self.userID))
        print("{:<12} {:1} {:<36}".format("sessionID", "=", self.sessionID))
        print("{:<12} {:1} {:<36}".format("entryID", "=", self.entryID))
        print("{:<12} {:1} {:<36}".format("date","=", self.date))
        print("{:<12} {:1} {:<36}".format("patternID", "=", self.patternID))
        print("{:<12} {:1} {:<36}".format("result", "=", self.result))
        print("{:<12} {:1} {:<36}".format("responseTime", "=", self.responseTime))