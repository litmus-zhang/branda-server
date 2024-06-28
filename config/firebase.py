from firebase_admin import credentials, firestore, initialize_app, auth
from firebase_admin.auth import Client
import os


if os.environ.get("development"):
    os.environ["FIREBASE_AUTH_EMULATOR_HOST"] = "localhost:9099"
    os.environ["FIRESTORE_EMULATOR_HOST"] = "localhost:8080"


def init_firebase():
    cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))

    default_app = initialize_app(cred)
    db = firestore.client(app=default_app)
    # initialize auth
    auth = Client(app=default_app)
    if os.environ.get("development"):
        db._firestore_client._emulator_host = "localhost:8080"
        os.environ["FIREBASE_AUTH_EMULATOR_HOST"] = "localhost:9099"
        # replace with your emulator host and port
    return db, auth


# Function to clear Firestore data
def clear_firestore_data():
    db = firestore.client()
    # Add logic to delete documents from your collections
    # Example: Delete all documents from 'users' collection
    users_ref = db.collection("users")
    brands_ref = db.collection("brands")
    docs = users_ref.stream()
    docs2 = brands_ref.stream()
    for doc in docs:
        doc.reference.delete()
    for doc in docs2:
        doc.reference.delete()


# Function to delete all users from Firebase Authentication
def delete_all_auth_users():
    user_list = auth.list_users().iterate_all()
    for user in user_list:
        auth.delete_user(user.uid)
