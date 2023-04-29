import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK with service account credentials
cred = credentials.Certificate("PyBrains/base_config.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pybrains-6cd3a-default-rtdb.europe-west1.firebasedatabase.app/'
})

# Get a reference to the root node of your Firebase Realtime Database
ref = db.reference()

main_ref = ref.child("Test")


text = input("Write Text... ")



main_ref.push({"name": text})



input("DONE CLICK ENTER TO FINISH SCRIPT...")