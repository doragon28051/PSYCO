import firebase_admin
from firebase_admin import firestore, credentials
from flask import Flask

app = Flask(__name__)


#FIRESTORE
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
data_psycho = {} #temp place for storing psychologists data


# /psycho API endpoint with GET http request
# This API return list of all pyschologists information
@app.route('/psycho', methods=['GET'])
def get_pyscho():
    try:
        psychos = db.collection("psycho").stream()
        array_psycho = []
        for psycho in psychos:
            # will change later
            array_psycho.append({"namaPsycho:":psycho.get("namaPsycho"), "alamatPsycho":psycho.get("alamatPsycho"), "kontakPsycho":psycho.get("kontakPsycho")}) 
            data_psycho.update({"psychoList": array_psycho})
            return data_psycho
    except Exception as e:
        return f"Error occured: {e}"