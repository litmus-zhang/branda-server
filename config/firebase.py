from firebase_admin import credentials, firestore, initialize_app
from firebase_admin.auth import Client
import os

# Replace 'path/to/your/serviceAccountKey.json' with the actual path


os.environ["FIREBASE_AUTH_EMULATOR_HOST"] = "localhost:9099"
os.environ["FIRESTORE_EMULATOR_HOST"] = "localhost:8080"


def init_firebase():
    cred = credentials.Certificate(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))

    default_app = initialize_app(cred)
    db = firestore.client(app=default_app)
    # initialize auth
    auth = Client(app=default_app)
    # if os.environ.get('development'):
    #     db._firestore_client._emulator_host = 'localhost:8080'
    #     os.environ["FIREBASE_AUTH_EMULATOR_HOST"] = "localhost:9099"
    #     # replace with your emulator host and port
    return db, auth
