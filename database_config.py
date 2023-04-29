import firebase_admin
from firebase_admin import credentials, db
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

# Initialize Firebase Admin SDK with service account credentials
cred = credentials.Certificate("base_config.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pybrains-6cd3a-default-rtdb.europe-west1.firebasedatabase.app/'
})

# Get a reference to the root node of your Firebase Realtime Database
ref = db.reference()

main_ref = ref.child("Test")


root = tk.Tk()
root.title("Import Image")
root.geometry("300x300")

def import_image():
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    image.show()

button = tk.Button(root, text="Import Image", command=import_image)
button.pack()




