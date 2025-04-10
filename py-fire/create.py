import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc = {
  "name": "王珮淳",
  "mail": "s1108707@pu.edu.tw",
  "lab": 77
}

#doc_ref = db.collection("靜宜資管").document("tcyang")
#doc_ref.set(doc)

collection_ref = db.collection("靜宜資管")
collection_ref.add(doc)
