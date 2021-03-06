from datetime import datetime
import uuid

class FlashCardEntry:

    def __init__(self,
                 patternID,
                 userID,
                 sessionID):

        #  set generated values
        entryID = "entry-"+str(uuid.uuid4())
        self.start_time = datetime.now()

        # set placeholders
        responseTime = -1
        result = -1
        
        self.userID = userID
        self.sessionID = sessionID
        self.entryID = entryID
        self.date = self.start_time.strftime("%d/%m/%Y %H:%M:%S")
        self.patternID = patternID
        self.result = result
        self.responseTime = responseTime

    def setDoneTime(self):
        done_time = datetime.now()
        self.responseTime = (done_time - self.start_time).microseconds // 1000

    def addResult(self, correct : bool):
        # check if the response time was added
        assert self.responseTime != -1, "responseTime not yet set"

        # set the result
        self.result = int(correct)

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