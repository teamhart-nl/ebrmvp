import firebase_admin
#from firebase_admin import db
from firebase_admin import credentials, firestore

class Database:

	def __init__(self):

		cred = firebase_admin.credentials.Certificate("ebrmvp-firebase-adminsdk-rav0e-86494e7c9e.json")
		firebase_admin.initialize_app(cred, {
			'projectId': 'ebrmvp',
		})

		self.db = firestore.client()
		self.homeRef = self.db.collection(u"training-entries")

	def addEntry(self, fcEntry):
		self.homeRef.add(fcEntry.getEntryDict())

