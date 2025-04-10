import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

x = input("請輸入查詢老師:")
collection_ref = db.collection("靜宜資管")
docs = collection_ref.where(filter=FieldFilter("name","==", x)).get()
for doc in docs:
    print("文件內容：{}".format(doc.to_dict()))
