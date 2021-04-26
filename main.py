from Database import Database
from FlashCardEntry import FlashCardEntry

if __name__ == '__main__':
    # creating an entry
    fcEntry = FlashCardEntry()
    fcEntry.printEntry()

    # adding it to the database
    database = Database()
    database.addEntry(fcEntry)
