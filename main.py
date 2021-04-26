from tkinter import *

#from Database import Database
from FlashCardEntry import FlashCardEntry
from PatternStore import PatternStore

class GUI:

    def __init__(self):
        # creating an entry
        #fcEntry = FlashCardEntry()
        #fcEntry.printEntry()

        # adding it to the database
        #self.database = Database()
        #self.database.addEntry(fcEntry)

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
        pattern = self.pattern_store.getRandomPattern()
        self.current_pattern = pattern

        # initialize current flashcard entry

        self.btn_show_card.configure(state="active")
        self.btn_random_pattern.configure(state="disabled")

    def showCardClicked(self):
        self.lbl.configure(text=self.current_pattern)

        self.btn_correct.configure(state="active")
        self.btn_incorrect.configure(state="active")

    def correctClicked(self):
        print("t was correct")

        self.lbl.configure(text="hidden")

        self.btn_random_pattern.configure(state="active")
        self.btn_correct.configure(state="disabled")
        self.btn_incorrect.configure(state="disabled")

    def incorrectClicked(self):
        print("t was incorrect")

        self.lbl.configure(text="hidden")

        self.btn_random_pattern.configure(state="active")
        self.btn_correct.configure(state="disabled")
        self.btn_incorrect.configure(state="disabled")

if __name__ == "__main__":
    gui = GUI()