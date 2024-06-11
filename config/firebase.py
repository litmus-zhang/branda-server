import firebase_admin
from firebase_admin import credentials, firestore, auth, initialize_app
from firebase_admin.auth import Client
import os

# Replace 'path/to/your/serviceAccountKey.json' with the actual path


def init_firebase():
    cred = credentials.Certificate(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))

    default_app = initialize_app(cred)
    db = firestore.client(app=default_app)


    # initialize auth
    auth = Client(app=default_app)

    return db, auth
