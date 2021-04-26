from tkinter import *
import uuid
import pickle
import os

from Database import Database
from FlashCardEntry import FlashCardEntry
from PatternStore import PatternStore

class GUI:

    def __init__(self):
        # initialize database
        self.database = Database()

        # set session id 
        self.session_id = "session-"+str(uuid.uuid4())

        # get persisent user id
        self.user_id = self._getUserID()

        #interface for getting patterns
        self.pattern_store = PatternStore()

        # UI
        window = Tk()
        window.title("Extremely Basic Rudimentary Minimum Viable Product")
        window.geometry('350x200')
        
        # feel pattern
        self.btn_random_pattern = Button(window, text="Feel a random pattern", command=self.newPatternClicked)
        self.btn_random_pattern.grid(column=1, row=0)

        # Pattern display
        self.lbl = Label(window, text="hidden")
        self.lbl.grid(column=0, row=1)

        # show flas card
        self.btn_show_card = Button(window, text="Show Pattern", command=self.showCardClicked, state="disabled")
        self.btn_show_card.grid(column=1, row=1)

        # make choice - correct
        self.btn_correct = Button(window, text="'twas right'", command=self.correctClicked, state="disabled")
        self.btn_correct.grid(column=0, row=2)

        # make choice - incorrect
        self.btn_incorrect = Button(window, text="'twas wrong'", command=self.incorrectClicked, state="disabled")
        self.btn_incorrect.grid(column=1, row=2)

        # main GUI loop
        window.mainloop()

    def newPatternClicked(self):
        # get a random pattern from PatternStore
        self.current_pattern = self.pattern_store.getRandomPattern()
        # initialize current flashcard entry
        self.current_flashcard = FlashCardEntry(patternID=self.current_pattern, 
                                                userID = self.user_id, 
                                                sessionID = self.session_id)

        self.btn_show_card.configure(state="active")
        self.btn_random_pattern.configure(state="disabled")

    def showCardClicked(self):
        #set the response time of entry
        self.current_flashcard.setDoneTime()

        # display the pattern that was sent
        self.lbl.configure(text=self.current_pattern)

        # update GUI to verification state
        self.btn_correct.configure(state="active")
        self.btn_incorrect.configure(state="active")

    def correctClicked(self):
        print("t was correct")

        # finish current flashcard
        self.current_flashcard.addResult(correct = True)

        # send flashcard to database
        self._sendCurrentFlashCard()

        # update GUI to starting state
        self.lbl.configure(text="hidden")
        self.btn_random_pattern.configure(state="active")
        self.btn_correct.configure(state="disabled")
        self.btn_incorrect.configure(state="disabled")
        self.btn_show_card.configure(state="disabled")

    def incorrectClicked(self):
        print("t was incorrect")

        # finish current flashcard
        self.current_flashcard.addResult(correct = False)

        # send flashcard to database
        self._sendCurrentFlashCard()

        # update GUI to starting state
        self.lbl.configure(text="hidden")
        self.btn_random_pattern.configure(state="active")
        self.btn_correct.configure(state="disabled")
        self.btn_incorrect.configure(state="disabled")
        self.btn_show_card.configure(state="disabled")

    def _sendCurrentFlashCard(self):
        print("sending following entry to database")
        self.current_flashcard.printEntry()

        self.database.addEntry(self.current_flashcard)

    '''
    Checks if first local run; if so makes userid else read its in
    '''
    def _getUserID(self):
        if "user.id" in os.listdir(os.getcwd()):
            with open("user.id", 'rb') as f:
                return str(pickle.load(f))
        else:
            userid = "user-"+str(uuid.uuid4())
            with open("user.id", 'wb')  as f:
                pickle.dump(userid, f)
            return userid
    

if __name__ == "__main__":
    gui = GUI()